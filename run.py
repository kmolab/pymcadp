if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    from main.main import MainWindow
    
    app = QApplication(sys.argv)
    
    main = MainWindow()
    main.show()
    # for Python 2.7 exec is a keyword, not for Python 3
    # but PyQt5 has exec_() which is for Python 2.7 which is the same as exec()
    # ref: https://docs.python.org/2.7/reference/lexical_analysis.html#keywords
    # ref: https://docs.python.org/3/reference/lexical_analysis.html#keywords
    # for Python 3 and PyQt5 can use exec() or exec_()
    sys.exit(app.exec())
