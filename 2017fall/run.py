import sys
from PyQt5 import QtWidgets
from ui import Dialog

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #win = QtWidgets.QWidget()
    win = Dialog.Dialog()
    win.show()
    sys.exit(app.exec())
