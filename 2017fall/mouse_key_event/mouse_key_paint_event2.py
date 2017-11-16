import sys
from PyQt5.QtWidgets import QWidget , QApplication
from PyQt5.QtGui import QPainter , QPen
from PyQt5.QtCore import Qt
from math import sin , cos , pi

class MyWidget ( QWidget ):
    def __init__ ( self ):
        super () .  __init__ ()
        self .  resize ( 500 , 500 )

    def paintEvent ( self , event ):
        p = QPainter ()
        p .  begin ( self )
        pen = QPen ( Qt . red , 10 )
        p .  setPen ( pen )

        for i in range ( 4 ):
            p .  drawPoint (
            250 + 200 * cos ( pi / 4 + pi / 2 * i ),
            250 + 200 * sin ( pi / 4 + pi / 2 * i )
            )
        p .  end ()

def main ():
    app = QApplication ( sys.argv )
    w = MyWidget ()
    w .  show ()
    sys .  exit ( app . exec_ ())

if __name__ == "__main__" :
    main ()