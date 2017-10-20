# -*- coding: utf-8 -*-

"""
Module implementing Direction.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_direction import Ui_Dialog

from vrep_linefollower import VrepLineFollower

class Direction(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Direction, self).__init__(parent)
        self.setupUi(self)
        self.line_follower = VrepLineFollower()
        # 利用迴圈連接按鈕 signal 與 slot
        for i in [self.up,  self.down,  self.right,  self.left]:
            i.clicked.connect(self.control)
        
    def control (self):
        # self.sender 為與各按鈕對應, 滑鼠按各 button 後送出 signal 的對應物件
        direction = self.sender()
        # 利用 text() 方法取得各送出 signal 物件 sender 所對應的 button text 文字設定
        self.line_follower.to_direction(direction.text())
        self.lineEdit.setText(direction.text())
