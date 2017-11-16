import sys
from PyQt5.QtWidgets import QWidget , QApplication
from PyQt5.QtGui import QPainter , QPen
from PyQt5.QtCore import Qt , QTimer
from math import sin , cos , pi

class MyWidget ( QWidget ):
    def __init__ ( self ):
        super ().__init__ ()
        self.timer = QTimer ()
        self.timer.timeout.connect ( self . process_timeout )
        self.timer.start ( 50 ) # 50 - the period in milliseconds
        self.phi = 0 # The angle in radians.
        self.resize ( 500 , 500 )

    def process_timeout ( self ):
        self.phi += 0.01
        self.update ()

    def paintEvent ( self , e ):
        p = QPainter ()
        p.begin ( self )
        pen = QPen ( Qt . red , 10 )
        p.setPen ( pen )

        for i in range ( 4 ):
            angle = ( self.phi + pi / 4 + pi / 2 * i )
            p.drawPoint (
            250 + 200 * cos ( angle ),
            250 + 200 * sin ( angle )
            )

        p.end ()

def main ():
    app = QApplication ( sys.argv )
    w = MyWidget ()
    w.show ()
    sys.exit ( app . exec_ ())

if __name__ == "__main__" :
    main ()