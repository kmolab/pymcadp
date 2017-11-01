# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\fossil\wd\pymcadp\v-rep\v-rep_pyqt5_linefollower\direction.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(463, 275)
        Dialog.setSizeGripEnabled(True)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 261, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 60, 81, 16))
        self.label.setObjectName("label")
        self.up = QtWidgets.QPushButton(Dialog)
        self.up.setGeometry(QtCore.QRect(180, 120, 93, 28))
        self.up.setObjectName("up")
        self.left = QtWidgets.QPushButton(Dialog)
        self.left.setGeometry(QtCore.QRect(110, 160, 93, 28))
        self.left.setObjectName("left")
        self.right = QtWidgets.QPushButton(Dialog)
        self.right.setGeometry(QtCore.QRect(250, 160, 93, 28))
        self.right.setObjectName("right")
        self.down = QtWidgets.QPushButton(Dialog)
        self.down.setGeometry(QtCore.QRect(180, 200, 93, 28))
        self.down.setObjectName("down")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Cart IP:port:"))
        self.up.setText(_translate("Dialog", "up"))
        self.left.setText(_translate("Dialog", "left"))
        self.right.setText(_translate("Dialog", "right"))
        self.down.setText(_translate("Dialog", "down"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

