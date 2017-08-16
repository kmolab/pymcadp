# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\test\menu_dialog\calculator\simple_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.one = QtWidgets.QPushButton(Dialog)
        self.one.setGeometry(QtCore.QRect(70, 110, 75, 23))
        self.one.setObjectName("one")
        self.display = QtWidgets.QLineEdit(Dialog)
        self.display.setGeometry(QtCore.QRect(70, 30, 231, 51))
        self.display.setObjectName("display")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Simple Calculator"))
        self.one.setText(_translate("Dialog", "1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

