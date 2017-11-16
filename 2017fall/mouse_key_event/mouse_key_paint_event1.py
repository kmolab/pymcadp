import sys
from PyQt5.QtWidgets import QWidget , QApplication
from PyQt5.QtGui import QPainter , QPen
from PyQt5.QtCore import Qt

class MyWidget ( QWidget ):
    
    def __init__ ( self ):
         super () .  __init__ ()
         self .  points = []

    def mousePressEvent ( self , e ):
         print ( "Mousepressed at" , e.x (), e . y ())
         self .  points .  append ([ e .x (), e . y ()])
         self .  update () # all redraw only through update,
                       # which itself calls paintEvent.

    def mouseReleaseEvent ( self , e ):
        print ( "Mouse released at" , e . x (), e . y ())

    def mouseMoveEvent ( self , e ):
         print ( "Mouse moved to" , e . x (), e . y ())

    def keyPressEvent ( self , e ):
        if e .  key () == Qt .  Key_Left :
             print ( 'Left' )
        elif e .  key () == Qt .  Key_Right :
             print ( 'Right' )
        elif e .  key () == Qt .  Key_Up :
             print ( 'Up' )
        elif e .  key () == Qt .  Key_Down :
             print ( 'Down' )
        print ( "Key pressed, text is" , repr ( e . text ()))

    def keyReleaseEvent ( self , e ):
        print ( "Key released, text is" , repr ( e . text ()))

    def paintEvent ( self , e ):
        p = QPainter ()
        p .  begin ( self )
        pen = QPen ( Qt . red , 10 )
        p .  setPen ( pen )

        for x , y in self .  points :
            p .  drawPoint ( x , y )

        p .  end ()

def main ():
    app = QApplication ( sys.argv )
    w = MyWidget ()
    w .  show ()
    sys .  exit ( app . exec_ ())

if __name__ == "__main__" :
    main ()