# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\tmp\currency_exchange\ui\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 250)
        Dialog.setMinimumSize(QtCore.QSize(600, 250))
        Dialog.setMaximumSize(QtCore.QSize(600, 250))
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.fromspinBox = QtWidgets.QSpinBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.fromspinBox.setFont(font)
        self.fromspinBox.setObjectName("fromspinBox")
        self.gridLayout.addWidget(self.fromspinBox, 1, 2, 1, 1)
        self.tocomboBox = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tocomboBox.setFont(font)
        self.tocomboBox.setObjectName("tocomboBox")
        self.gridLayout.addWidget(self.tocomboBox, 3, 0, 1, 2)
        self.fromcomboBox = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.fromcomboBox.setFont(font)
        self.fromcomboBox.setObjectName("fromcomboBox")
        self.gridLayout.addWidget(self.fromcomboBox, 1, 0, 1, 2)
        self.tolabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tolabel.setFont(font)
        self.tolabel.setText("")
        self.tolabel.setObjectName("tolabel")
        self.gridLayout.addWidget(self.tolabel, 3, 2, 1, 1)
        self.datelabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.datelabel.setFont(font)
        self.datelabel.setText("")
        self.datelabel.setObjectName("datelabel")
        self.gridLayout.addWidget(self.datelabel, 0, 0, 1, 3)

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

