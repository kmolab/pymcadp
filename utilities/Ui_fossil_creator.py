# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\fossil\wd\pymcadp\utilities\fossil_creator.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fossilCreator(object):
    def setupUi(self, fossilCreator):
        fossilCreator.setObjectName("fossilCreator")
        fossilCreator.resize(542, 386)
        self.buttonBox = QtWidgets.QDialogButtonBox(fossilCreator)
        self.buttonBox.setGeometry(QtCore.QRect(170, 340, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.getstudfile = QtWidgets.QPushButton(fossilCreator)
        self.getstudfile.setGeometry(QtCore.QRect(20, 12, 91, 21))
        self.getstudfile.setObjectName("getstudfile")
        self.displaytab = QtWidgets.QTabWidget(fossilCreator)
        self.displaytab.setGeometry(QtCore.QRect(130, 90, 401, 241))
        self.displaytab.setObjectName("displaytab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.studentlist = QtWidgets.QTextEdit(self.tab)
        self.studentlist.setGeometry(QtCore.QRect(3, 0, 391, 211))
        self.studentlist.setObjectName("studentlist")
        self.displaytab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.wikilinks = QtWidgets.QTextEdit(self.tab_2)
        self.wikilinks.setGeometry(QtCore.QRect(0, 0, 401, 221))
        self.wikilinks.setObjectName("wikilinks")
        self.displaytab.addTab(self.tab_2, "")
        self.generatelinks = QtWidgets.QPushButton(fossilCreator)
        self.generatelinks.setGeometry(QtCore.QRect(20, 90, 91, 23))
        self.generatelinks.setObjectName("generatelinks")
        self.sendnotice = QtWidgets.QPushButton(fossilCreator)
        self.sendnotice.setGeometry(QtCore.QRect(20, 50, 91, 23))
        self.sendnotice.setObjectName("sendnotice")
        self.passpath = QtWidgets.QLineEdit(fossilCreator)
        self.passpath.setGeometry(QtCore.QRect(320, 40, 211, 20))
        self.passpath.setObjectName("passpath")
        self.label = QtWidgets.QLabel(fossilCreator)
        self.label.setGeometry(QtCore.QRect(260, 40, 47, 13))
        self.label.setObjectName("label")
        self.getpasspath = QtWidgets.QPushButton(fossilCreator)
        self.getpasspath.setGeometry(QtCore.QRect(140, 40, 111, 23))
        self.getpasspath.setObjectName("getpasspath")
        self.label_2 = QtWidgets.QLabel(fossilCreator)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 91, 21))
        self.label_2.setObjectName("label_2")
        self.emailaddress = QtWidgets.QLineEdit(fossilCreator)
        self.emailaddress.setGeometry(QtCore.QRect(240, 10, 291, 20))
        self.emailaddress.setObjectName("emailaddress")
        self.executestatus = QtWidgets.QTextEdit(fossilCreator)
        self.executestatus.setGeometry(QtCore.QRect(20, 120, 104, 211))
        self.executestatus.setObjectName("executestatus")

        self.retranslateUi(fossilCreator)
        self.displaytab.setCurrentIndex(1)
        self.buttonBox.accepted.connect(fossilCreator.accept)
        self.buttonBox.rejected.connect(fossilCreator.reject)
        QtCore.QMetaObject.connectSlotsByName(fossilCreator)

    def retranslateUi(self, fossilCreator):
        _translate = QtCore.QCoreApplication.translate
        fossilCreator.setWindowTitle(_translate("fossilCreator", "Fossil Creator"))
        self.getstudfile.setText(_translate("fossilCreator", "Ｇｅｔ　Ｓｔｕｄ　Ｆｉｌｅ"))
        self.displaytab.setTabText(self.displaytab.indexOf(self.tab), _translate("fossilCreator", "Student List"))
        self.displaytab.setTabText(self.displaytab.indexOf(self.tab_2), _translate("fossilCreator", "Wiki Links"))
        self.generatelinks.setText(_translate("fossilCreator", "Generate Links"))
        self.sendnotice.setText(_translate("fossilCreator", "Send Notice"))
        self.label.setText(_translate("fossilCreator", "Pass File:"))
        self.getpasspath.setText(_translate("fossilCreator", "Get Password File"))
        self.label_2.setText(_translate("fossilCreator", "Send Mail Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fossilCreator = QtWidgets.QDialog()
    ui = Ui_fossilCreator()
    ui.setupUi(fossilCreator)
    fossilCreator.show()
    sys.exit(app.exec_())

