# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\fossil\wd\pymcadp\cad_2d\cad_2d.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cad2d(object):
    def setupUi(self, cad2d):
        cad2d.setObjectName("cad2d")
        cad2d.resize(763, 764)
        self.graphicsView = QtWidgets.QGraphicsView(cad2d)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 741, 681))
        self.graphicsView.setObjectName("graphicsView")
        self.clearview = QtWidgets.QPushButton(cad2d)
        self.clearview.setGeometry(QtCore.QRect(290, 710, 141, 41))
        self.clearview.setObjectName("clearview")

        self.retranslateUi(cad2d)
        QtCore.QMetaObject.connectSlotsByName(cad2d)

    def retranslateUi(self, cad2d):
        _translate = QtCore.QCoreApplication.translate
        cad2d.setWindowTitle(_translate("cad2d", "CAD　２Ｄ"))
        self.clearview.setText(_translate("cad2d", "Clear View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cad2d = QtWidgets.QDialog()
    ui = Ui_cad2d()
    ui.setupUi(cad2d)
    cad2d.show()
    sys.exit(app.exec_())

