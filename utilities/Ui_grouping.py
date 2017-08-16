# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\test\menu_dialog\utilities\grouping.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ok(object):
    def setupUi(self, ok):
        ok.setObjectName("ok")
        ok.resize(574, 579)
        ok.setSizeGripEnabled(True)
        self.gridLayoutWidget = QtWidgets.QWidget(ok)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 521, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.getfile = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.getfile.setObjectName("getfile")
        self.gridLayout.addWidget(self.getfile, 0, 0, 1, 1)
        self.display = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.display.setObjectName("display")
        self.filecontent_tab = QtWidgets.QWidget()
        self.filecontent_tab.setObjectName("filecontent_tab")
        self.filecontent = QtWidgets.QPlainTextEdit(self.filecontent_tab)
        self.filecontent.setGeometry(QtCore.QRect(3, 0, 431, 521))
        self.filecontent.setObjectName("filecontent")
        self.display.addTab(self.filecontent_tab, "")
        self.groups_tab = QtWidgets.QWidget()
        self.groups_tab.setObjectName("groups_tab")
        self.groups = QtWidgets.QPlainTextEdit(self.groups_tab)
        self.groups.setGeometry(QtCore.QRect(3, 0, 431, 531))
        self.groups.setObjectName("groups")
        self.display.addTab(self.groups_tab, "")
        self.seats_tab = QtWidgets.QWidget()
        self.seats_tab.setObjectName("seats_tab")
        self.seats = QtWidgets.QTextEdit(self.seats_tab)
        self.seats.setGeometry(QtCore.QRect(-7, 0, 441, 531))
        self.seats.setObjectName("seats")
        self.display.addTab(self.seats_tab, "")
        self.gridLayout.addWidget(self.display, 0, 1, 3, 1)

        self.retranslateUi(ok)
        self.display.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(ok)

    def retranslateUi(self, ok):
        _translate = QtCore.QCoreApplication.translate
        ok.setWindowTitle(_translate("ok", "Grouping"))
        self.pushButton.setText(_translate("ok", "OK"))
        self.getfile.setText(_translate("ok", "Get File"))
        self.display.setTabText(self.display.indexOf(self.filecontent_tab), _translate("ok", "File Content"))
        self.display.setTabText(self.display.indexOf(self.groups_tab), _translate("ok", "Groups"))
        self.display.setTabText(self.display.indexOf(self.seats_tab), _translate("ok", "Seats"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ok = QtWidgets.QDialog()
    ui = Ui_ok()
    ui.setupUi(ok)
    ok.show()
    sys.exit(app.exec_())

