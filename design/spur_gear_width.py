# -*- coding: utf-8 -*-

"""
Module implementing gearWidth.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_spur_gear_width import Ui_gearWidth


class gearWidth(QDialog, Ui_gearWidth):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(gearWidth, self).__init__(parent)
        self.setupUi(self)
        self.calculate.clicked.connect(self.widthCalculate)
        
    def widthCalculate(self):
        # lineEdit value is text(), need to set default value for each lineEdit form field
        try:
            if self.power_to_transmit.text():
                power = float(self.power_to_transmit.text())
            else:
                power = 0
            no = int(self.no_of_pinion.text())
            mo = int(self.module.text())
            pa = float(self.pressure_angle.text())
            # 導入資料庫後材料將會從資料庫中取得後列入
            ma = float(self.material.value())
            sf = float(self.safety_factor.text())
            self.gear_width.setText("Gear Width is :" + str(power*no*mo*pa*ma*sf))
        except:
            self.gear_width.setText("no answer")
        
