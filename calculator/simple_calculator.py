# -*- coding: utf-8 -*-

"""
Module implementing simpleCalculator.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_simple_calculator import Ui_Dialog


class simpleCalculator(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(simpleCalculator, self).__init__(parent)
        self.setupUi(self)
        self.one.clicked.connect(self.num)

    def num(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())
        self.display.setText(str(digitValue))
