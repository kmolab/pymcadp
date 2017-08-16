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
