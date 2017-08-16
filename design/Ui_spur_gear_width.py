# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\test\menu_dialog\design/spur_gear_width.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gearWidth(object):
    def setupUi(self, gearWidth):
        gearWidth.setObjectName("gearWidth")
        gearWidth.resize(497, 432)
        gearWidth.setSizeGripEnabled(True)
        self.formLayoutWidget = QtWidgets.QWidget(gearWidth)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 40, 351, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.power_to_transmit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.power_to_transmit.setObjectName("power_to_transmit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.power_to_transmit)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.no_of_pinion = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.no_of_pinion.setObjectName("no_of_pinion")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.no_of_pinion)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.module = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.module.setObjectName("module")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.module)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pressure_angle = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pressure_angle.setObjectName("pressure_angle")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pressure_angle)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.material = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.material.setObjectName("material")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.material)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.safety_factor = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.safety_factor.setObjectName("safety_factor")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.safety_factor)
        self.calculate = QtWidgets.QPushButton(self.formLayoutWidget)
        self.calculate.setObjectName("calculate")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.calculate)
        self.gear_width = QtWidgets.QTextEdit(gearWidth)
        self.gear_width.setGeometry(QtCore.QRect(73, 260, 361, 131))
        self.gear_width.setObjectName("gear_width")

        self.retranslateUi(gearWidth)
        QtCore.QMetaObject.connectSlotsByName(gearWidth)

    def retranslateUi(self, gearWidth):
        _translate = QtCore.QCoreApplication.translate
        gearWidth.setWindowTitle(_translate("gearWidth", "Gear Width Design"))
        self.label_6.setText(_translate("gearWidth", "Power to Transmit"))
        self.label.setText(_translate("gearWidth", "Number of Pinion"))
        self.label_2.setText(_translate("gearWidth", "Module of Gear"))
        self.label_3.setText(_translate("gearWidth", "Pressure Angle"))
        self.label_4.setText(_translate("gearWidth", "Material"))
        self.label_5.setText(_translate("gearWidth", "Safety Factor"))
        self.calculate.setText(_translate("gearWidth", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gearWidth = QtWidgets.QDialog()
    ui = Ui_gearWidth()
    ui.setupUi(gearWidth)
    gearWidth.show()
    sys.exit(app.exec_())

