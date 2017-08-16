# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\test\menu_dialog\calculator\engr_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EngrCalculator(object):
    def setupUi(self, EngrCalculator):
        EngrCalculator.setObjectName("EngrCalculator")
        EngrCalculator.resize(400, 300)
        EngrCalculator.setSizeGripEnabled(True)
        self.display = QtWidgets.QLineEdit(EngrCalculator)
        self.display.setGeometry(QtCore.QRect(80, 40, 241, 41))
        self.display.setObjectName("display")
        self.one = QtWidgets.QPushButton(EngrCalculator)
        self.one.setGeometry(QtCore.QRect(80, 110, 75, 23))
        self.one.setObjectName("one")

        self.retranslateUi(EngrCalculator)
        QtCore.QMetaObject.connectSlotsByName(EngrCalculator)

    def retranslateUi(self, EngrCalculator):
        _translate = QtCore.QCoreApplication.translate
        EngrCalculator.setWindowTitle(_translate("EngrCalculator", "Engr Calculator"))
        self.one.setText(_translate("EngrCalculator", "1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EngrCalculator = QtWidgets.QDialog()
    ui = Ui_EngrCalculator()
    ui.setupUi(EngrCalculator)
    EngrCalculator.show()
    sys.exit(app.exec_())

