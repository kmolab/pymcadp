# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
# 呼叫 calculator 目錄下的模組
from calculator.simple_calculator import simpleCalculator
from calculator.engr_calculator import engrCalculator
# 呼叫 utilities 目錄下的模組
from utilities.grouping import Grouping
from utilities.graphics_viewer import graphicsViewer
# 呼叫 design 目錄下的模組
from design.spur_gear_width import gearWidth
# 導入 cad_2d 目錄下的模組
from cad_2d.cad_2d import Cad2dMainWindow
# 導入 print 目錄下的模組
from paint.paint import Paint
# 導入 calculator 目錄中 cal_ex1.py 中的 Calculator
from calculator.cal_ex1 import Calculator

#呼叫本身目錄下的模組
from .Ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    
    @pyqtSlot()
    def on_actionSimple_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        ''' 除非關閉 calculator, 否則主視窗無法操作 (鎖定)'''
        calculator = simpleCalculator()
        calculator.exec()
  
        # 注意 exec() 與 show() 的差別
        # 若要使用 show(), 若無 self 則會閃退
        '''self.calculator 與主視窗為兩個獨立物件與案例'''
        '''
        self.calculator = Simple()
        self.calculator.show()
        '''
    
    @pyqtSlot()
    def on_actionQuit_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        # program closed
        self.close()
    
    @pyqtSlot()
    def on_actionEngr_Calculator_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        calculator = engrCalculator()
        calculator.exec()
    
    @pyqtSlot()
    def on_actionGrouping_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        grouping = Grouping()
        grouping.exec()
    
    @pyqtSlot()
    def on_actionGraphics_Viewer_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        graphicsviewer = graphicsViewer()
        graphicsviewer.exec()
    
    @pyqtSlot()
    def on_actionSpur_Gear_Width_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        gearwidth = gearWidth()
        gearwidth.exec()
    
    @pyqtSlot()
    def on_action2D_cad_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        # 若無 self, show() 會閃退, 
        # 成員變數案例, 使用 show() 為獨立物件
        # show() 後控制權即刻返還給呼叫的主物件, 因此成為獨立運作物件
        self.cad2dwin = Cad2dMainWindow()
        self.cad2dwin.show()
    
    @pyqtSlot()
    def on_actionPaint_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.paint = Paint()
        self.paint.show()
    
    @pyqtSlot()
    def on_actioncal_ex1_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        self.cal_ex1 = Calculator()
        self.cal_ex1.show()
