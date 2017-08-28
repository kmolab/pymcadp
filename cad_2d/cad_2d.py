# -*- coding: utf-8 -*-

"""
Module implementing Cad2dMainWindow.
"""

from PyQt5.QtCore import pyqtSlot, QRectF, QLineF, QPointF,  Qt
from PyQt5.QtWidgets import QMainWindow,  QGraphicsScene, QGraphicsLineItem
from PyQt5 import QtGui

from .Ui_cad_2d import Ui_MainWindow


class Cad2dMainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Cad2dMainWindow, self).__init__(parent)
        self.setupUi(self)
        # 透過繼承 ui_MainWindow 物件, 已經擁有 self.graphicsView 成員物件
        self.scene = QGraphicsScene()
        # 在 scene 中加入繪圖元件
        # 字串
        '''
        self.scene.addText("Hello, world!")
        # 矩形
        self.scene.addRect(QRectF(0, 0, 100, 100))
        # 畫直線
        self.scene.addItem(
            QGraphicsLineItem(QLineF(100,  100,  200,  300)))
        '''
        # 將畫面設定在視圖中
        self.graphicsView.setScene(self.scene)

    def mousePressEvent(self, event):
        self._start = event.pos()
        self.update()
        if event.button()==Qt.LeftButton:
            point=QPointF(event.pos().x(), event.pos().y())
            self.scene.addText(str(event.pos().x())+","+str(event.pos().y())).setPos(point)
        super(Cad2dMainWindow, self).mousePressEvent(event)
        
    def mouseReleaseEvent(self, event):
        print("mouse release event")
