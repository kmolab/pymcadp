# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\tmp\qspinbox\ui\Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 200)
        Dialog.setMinimumSize(QtCore.QSize(300, 200))
        Dialog.setMaximumSize(QtCore.QSize(300, 200))
        Dialog.setSizeGripEnabled(True)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(150, 40, 120, 120))
        self.spinBox.setMinimumSize(QtCore.QSize(120, 120))
        self.spinBox.setMaximumSize(QtCore.QSize(120, 120))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(500)
        self.spinBox.setObjectName("spinBox")
        self.dial = QtWidgets.QDial(Dialog)
        self.dial.setGeometry(QtCore.QRect(20, 50, 80, 80))
        self.dial.setMinimumSize(QtCore.QSize(80, 80))
        self.dial.setMaximumSize(QtCore.QSize(80, 80))
        self.dial.setMaximum(500)
        self.dial.setSingleStep(0)
        self.dial.setObjectName("dial")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

