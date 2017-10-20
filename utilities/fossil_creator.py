# -*- coding: utf-8 -*-

"""
Module implementing fossilCreator.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QFileDialog

from .Ui_fossil_creator import Ui_fossilCreator


class fossilCreator(QDialog, Ui_fossilCreator):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(fossilCreator, self).__init__(parent)
        self.setupUi(self)
        
        # 自行設定 signal and slot
        self.getstudfile.clicked.connect(self.getStudFile)
        self.generatelinks.clicked.connect(self.generateLinks)

    def getStudFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        if fileName:
            #print(fileName)
            #self.filecontent.setPlainText(fileName)
            # 開檔並取得檔案內容顯示在  filecontent PlainText Edit 區域
            with  open(fileName, 'r', encoding='utf-8') as infile:
                # 必須再設定開檔案副檔名並判別文字檔案或二位元檔案
                self.studentlist.setPlainText(infile.read())
            # 設定內容後顯示該 Tab 內容 (在三個 tab 中排序 0)
            self.displaytab.setCurrentIndex(0)

    def generateLinks(self):
        links = '''[https://www.google.com]
[https://mde1a1.kmol.info]
'''
        self.wikilinks.setPlainText(links)
