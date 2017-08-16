# -*- coding: utf-8 -*-

"""
Module implementing Grouping.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QFileDialog

from .Ui_grouping import Ui_ok


class Grouping(QDialog, Ui_ok):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Grouping, self).__init__(parent)
        self.setupUi(self)
        # 自行設定 signal and slot
        self.getfile.clicked.connect(self.getFile)

    def getFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        if fileName:
            #print(fileName)
            #self.filecontent.setPlainText(fileName)
            # 開檔並取得檔案內容顯示在  filecontent PlainText Edit 區域
            with  open(fileName, 'r', encoding='utf-8') as infile:
                # 必須再設定開檔案副檔名並判別文字檔案或二位元檔案
                self.filecontent.setPlainText(infile.read())
            # 設定內容後顯示該 Tab 內容 (在三個 tab 中排序 0)
            self.display.setCurrentIndex(0)
