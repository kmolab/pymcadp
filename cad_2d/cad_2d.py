# -*- coding: utf-8 -*-

"""
Module implementing cad2d.
"""

from PyQt5.QtCore import pyqtSlot, QRectF, QLineF, QPointF,  Qt
from PyQt5.QtWidgets import QDialog,  QGraphicsScene,  QGraphicsLineItem
from PyQt5 import QtGui

from .Ui_cad_2d import Ui_cad2d

# 繼承 QGraphicsScene 物件, 自行建立 cadscene
class cadscene(QGraphicsScene):
    def __init__(self, parent=None):
        # Python3 的語法, 執行 parent 的 __init__
        super().__init__()

    def mousePressEvent(self, event):
        # 滑鼠按下後存入內部變數 _start
        self._start = event.scenePos()
        # 印出線段起點座標
        point = self._start
        text = self.addSimpleText(
            '(%d, %d)' % (point.x(), point.y()))
        text.setBrush(Qt.red)
        text.setPos(point)
    
    def mouseReleaseEvent(self,  event):
        start = QPointF(self._start)
        end = QPointF(event.scenePos())
        self.addItem(
            QGraphicsLineItem(QLineF(start, end)))
        # 印出線段終點座標
        point = end
        text = self.addSimpleText(
            '(%d, %d)' % (point.x(), point.y()))
        text.setBrush(Qt.red)
        text.setPos(point)

class cad2d(QDialog, Ui_cad2d):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(cad2d, self).__init__(parent)
        self.setupUi(self)
        #self.scene = QGraphicsScene()
        self.scene = cadscene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setSceneRect(QRectF(self.graphicsView.viewport().rect()))
        # 建立 clearview 按鈕對應的 signal 與 slot 
        self.clearview.clicked.connect(self.clearView)
    '''
    def mousePressEvent(self, event):
        self._start = event.pos()
        self.update()
        if event.button()==Qt.LeftButton:
            point=QPointF(event.pos().x(), event.pos().y())
            self.scene.addText(str(event.pos().x())+","+str(event.pos().y())).setPos(event.pos())
        super(cad2d, self).mousePressEvent(event)
    '''
    def clearView(self):
        self.scene.clear()
