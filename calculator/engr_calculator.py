# -*- coding: utf-8 -*-

"""
Module implementing engrCalculator.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_engr_calculator import Ui_EngrCalculator


class engrCalculator(QDialog, Ui_EngrCalculator):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(engrCalculator, self).__init__(parent)
        self.setupUi(self)
