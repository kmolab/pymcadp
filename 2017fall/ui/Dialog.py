# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_Dialog import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        # 當多個 signal 同時指向同一個 slot 處理時, 採用 for loop
        num_button = [self.one,  self.two,  \
        self.three,  self.four,  self.five,  self.six,  self.seven,  self.eight,  self.nine,  self.zero]
        plus_minus = [self.plus,  self.minus]
        multiply_divide = [self.multiply,  self.divide]
        #self.one.clicked.connect(self.number)
        # 數字按鍵的 signal 與 slot 設定
        for i in num_button:
            i.clicked.connect(self.number)
        
        # 加減鍵的 signal 與 slogt 設定
        for i in plus_minus:
            i.clicked.connect(self.additiveOperatorClicked)
        
        # 等於按鍵的 signal 與 slot 設定
        self.equal.clicked.connect(self.equalClicked)
        
        # 乘與除按建的 signal 與 slot 設定
        for i in multiply_divide:
            i.clicked.connect(self.multiplicativeOperatorClicked)
        
        # 等待運算的加或減
        self.pendingAdditiveOperator = ''
        self.sumSoFar = 0.0
        # 起始時, 等待使用者輸入運算數值變數為真
        self.waitingForOperand = True
        
        # 加入可以處理先乘除後加減的運算時, 新增暫存在記憶體的總數, sumInMemory
        # 以及暫存尚未完成運算的運算子 factorSoFar
        self.sumInMemory = 0.0
        self.factorSoFar = 0.0
        # 等待運算的乘或除
        self.pendingMultiplicativeOperator = ''
        
    def number(self):

        clickedButton = self.sender()
        digitValue = int(clickedButton.text())
        # when user clicks 0.0
        if self.display.text() == '0' and digitValue == 0.0:
            return
        
        # if under digit input process, clear display for the very first beginning
        # waitingForOperand 為 True 已經點按運算按鈕
        if self.waitingForOperand:
            # 清除 display 
            self.display.clear()
            # 將判斷是否已經點按運算按紐的判斷變數重新設為  False
            self.waitingForOperand = False
        # 利用 setText() 設定 LineEdit 元件顯示字串, 利用 text() 取出目前所顯示的字串, 同時也可利用 text() 擷取按鈕物件上顯示的字串
        #self.display.setText(self.display.text() + self.sender().text())
        self.display.setText(self.display.text() + str(digitValue))
        
    def additiveOperatorClicked(self):
        # 確定按下加或減
        clickedButton = self.sender()
        # 確定運算子, 為加或減
        clickedOperator = clickedButton.text()
        # 點按運算子之前在 display 上的數字, 為運算數
        operand = float(self.display.text())
        
        # 納入乘與除之後的先乘除後加減運算邏輯
        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''
            
            
        # 假如有等待運算的加或減, 進入執行運算
        # 若前面已經有運算數等待運算, 則執行計算
        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return
            # 顯示目前的運算結果
            self.display.setText(str(self.sumSoFar))
        else:
            # 假如仍未進入等待運算的階段, 則將運算數與 self.fumSoFar 對應
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        # 進入等待另外一個運算數的階段, 設為 True 才會清空 LineEdit
        self.waitingForOperand = True

    def multiplicativeOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand

        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True
    
    def equalClicked(self):
        # 從 display 取的運算數值
        operand = float(self.display.text())
        
        # 先乘除的運算處理
        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return
            # factorSoFar 為乘或除運算所得之暫存數值
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''
        
        # 若有等待加或減的運算子, 執行運算
        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True

    # 右運算數與等待運算子當作輸入
    def calculate(self, rightOperand, pendingOperator):
        # 進入計算流程時, 用目前輸入的運算數值與 self.sumSoFar 執行計算
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand

        elif pendingOperator == "*":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "/":
            if rightOperand == 0.0:
                return False

            self.factorSoFar /= rightOperand

        return True
