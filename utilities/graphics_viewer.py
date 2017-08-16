# -*- coding: utf-8 -*-

"""
Module implementing graphicsViewer.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QFileDialog,  QGraphicsScene,  QGraphicsPixmapItem
from PyQt5 import QtGui

# 利用 python -m pip install pillow 安裝 PIL 模組
from PIL import Image

from .Ui_graphics_viewer import Ui_graphics_viewer


class graphicsViewer(QDialog, Ui_graphics_viewer):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(graphicsViewer, self).__init__(parent)
        self.setupUi(self)
        self.getfile.clicked.connect(self.getFile)
        
    def getFile(self):
        self.image=None
        # 開啟圖片檔案
        # 設置檔案副檔名過濾, 使用雙分號間隔
        imgName,imgType= QFileDialog.getOpenFileName(self,
                                    "開啟圖片",
                                    "",
                                    " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

        #print(imgName)
        im=Image.open(imgName)
        self.image=imgName
        #print(im.size)
        scene=QGraphicsScene(self)
        pixmap=QtGui.QPixmap(imgName)
        #.scaled(im.size[1], im.size[1])
        item=QGraphicsPixmapItem(pixmap)
        scene.addItem(item)

        #png = QtGui.QPixmap(imgName).scaled(im.size[1], im.size[1])
        #self.graphicsView.scale(im.size[1], im.size[1])
        self.graphicsView.setScene(scene)
        #利用graphicsView显示图片
