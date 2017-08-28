# -*- coding: utf-8 -*-

"""
Module implementing Paint.
"""

from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter


from .Ui_paint import Ui_Form


class Paint(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Paint, self).__init__(parent)
        self.setupUi(self)
        
        self.px = None
        self.py = None
        self.points = []
        self.psets = []
        
    def mousePressEvent(self, event):
        self.points.append(event.pos())
        self.update()

    def mouseMoveEvent(self, event):
        self.points.append(event.pos())
        self.update()

    def mouseReleaseEvent(self, event):
        self.pressed = False
        self.psets.append(self.points)
        self.points = []
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)
        painter.drawRect(self.rect())

        painter.setPen(Qt.black)

        # draw historical points
        for points in self.psets:
            painter.drawPolyline(*points)

        # draw current points
        if self.points:
            painter.drawPolyline(*self.points)
