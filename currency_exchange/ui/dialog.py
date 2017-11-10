# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtWidgets import QDialog
from decimal import Decimal
from urllib.request import urlopen

from .Ui_dialog import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        
        date = self.getdata()
        rates = sorted(self.cur_code.keys())
        self.datelabel.setText(date)
        self.fromcomboBox.addItems(rates)
        self.fromspinBox.setRange(0.01, 10000000.00)
        self.fromspinBox.setValue(1.00)
        self.tocomboBox.addItems(rates)
        
        self.fromcomboBox.currentIndexChanged.connect(self.updateUi)
        self.tocomboBox.currentIndexChanged.connect(self.updateUi)
        self.fromspinBox.valueChanged.connect(self.updateUi)

    def updateUi(self):
        to = self.tocomboBox.currentText()
        from_ = self.fromcomboBox.currentText()
        to_code = self.cur_code[to]
        from_code = self.cur_code[from_]
        to_amt = Decimal(self.rates[to_code])
        from_amt = Decimal(self.rates[from_code])
        amt = Decimal(self.fromspinBox.value())
        amount = (from_amt/to_amt)*amt
        self.tolabel.setText("%0.2f" % amount)
        
    def getdata(self): 
        self.cur_code = {}
        try:
            date = "Unknown"
            file = urlopen("http://www.bankofcanada.ca/valet/observations/group/FX_RATES_DAILY/csv")
            file_handler = []
            
            for row in file:
                file_handler.append(row.decode())
            
            for row in file_handler:
                #print(row)
                if row.startswith("FX"):
                    line = row.split(",")
                    cur = line[2].split(" to")[0]
                    cur = cur[1:]
                    self.cur_code[cur.title()] = line[0]
                else:
                    continue
            header_list = []
            notFound = True
            x = 0
            while notFound:
                if file_handler[x].startswith("date"):
                    header = file_handler[x].split(",")
                    for col in header:
                        header_list.append(col.strip())
                    notFound = False
                x += 1
            data = []
            for row in file_handler[x:]:
                if row.startswith("\n"):
                    break
                else:
                    data = row.split(",")
            i = 0
            self.rates = {}
            for d in data:
                header = "".join(str(header_list[i]))
                self.rates[header] = d.strip()
                i += 1
            date = self.rates["date"]
            return "Exchange Rates Date: " + date
        except Exception as e:
            return ("Failed to download:\n%s" % e)
        finally:
            file.close()
