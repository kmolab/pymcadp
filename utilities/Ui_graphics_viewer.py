# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\test\menu_dialog\utilities/graphics_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_graphics_viewer(object):
    def setupUi(self, graphics_viewer):
        graphics_viewer.setObjectName("graphics_viewer")
        graphics_viewer.setWindowModality(QtCore.Qt.WindowModal)
        graphics_viewer.resize(581, 566)
        graphics_viewer.setSizeGripEnabled(True)
        self.getfile = QtWidgets.QPushButton(graphics_viewer)
        self.getfile.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.getfile.setObjectName("getfile")
        self.graphicsView = QtWidgets.QGraphicsView(graphics_viewer)
        self.graphicsView.setGeometry(QtCore.QRect(90, 10, 491, 551))
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(graphics_viewer)
        QtCore.QMetaObject.connectSlotsByName(graphics_viewer)

    def retranslateUi(self, graphics_viewer):
        _translate = QtCore.QCoreApplication.translate
        graphics_viewer.setWindowTitle(_translate("graphics_viewer", "Graphics Viewer"))
        self.getfile.setText(_translate("graphics_viewer", "get file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graphics_viewer = QtWidgets.QDialog()
    ui = Ui_graphics_viewer()
    ui.setupUi(graphics_viewer)
    graphics_viewer.show()
    sys.exit(app.exec_())

