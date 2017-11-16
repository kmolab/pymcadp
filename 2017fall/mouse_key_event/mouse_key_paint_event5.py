import sys
from PyQt5.QtWidgets import QWidget , QApplication
from PyQt5.QtGui import QPainter , QPen , QBrush , QColor , QPolygonF , QImage
from PyQt5.QtCore import Qt , QRectF , QPointF
from math import sin , cos , pi

class MyWidget ( QWidget ):
    def __init__ ( self ):
        super ().__init__ ()
        self.resize ( 500 , 500 )

    def paintEvent ( self , event ):
        # Create a QPainter and start drawing on the widget.
        p = QPainter ()
        p.begin ( self )
        # optional setting for drawing lines.  Drawing will go
        # slightly slower, but the lines themselves will be more smoothed.
        p.setRenderHint ( QPainter . Antialiasing )

        # Set the red handle to 2 pixels wide to draw a path
        p.setPen ( QPen ( QColor ( 255 , 0 , 0 ), 2 ))
        # Draw a point in the coordinate 30, 40.
        p.drawPoint ( QPointF ( 30 , 40 ))

        # Draw two parallel lines, one green, the other blue
        p.setPen ( QPen ( QColor ( 0 , 255 , 0 ), 2 ))
        p.drawLine ( QPointF ( 50 , 10 ), QPointF ( 100 , 110 ))
        p.setPen ( QPen ( QColor ( 0 , 0 , 255 ), 2 ))
        p.drawLine ( QPointF ( 70 , 10 ), QPointF ( 120 , 110 ))

        # Black handle 2 wide for the contour and a light red brush
        # for the inside of the shape
        p.setPen( QPen ( QColor ( 0 , 0 , 0 ), 2 ))
        p.setBrush( QBrush ( QColor ( 200, 100, 100)))
        # Draw a rectangle 50 by 50 with the upper left point (150, 40).
        p.drawRect ( QRectF ( 150 , 40 , 50 , 50 ))
        # Draw an ellipse centered at the point (270, 65) and semiaxes
        # 50 on X and 30 on Y.
        p.drawEllipse ( QPointF ( 270 , 65 ), 50 , 30 )

        # Draw a small straight triangle using
        # drawPolygon
        points = [ QPointF ( 50 , 350 ), QPointF ( 70 , 370 ), QPointF ( 50 , 390 )]
        polygon = QPolygonF ( points )
        p.drawPolygon ( polygon )

        p.drawText ( 50 , 200 , "Hello world!" )

        # Load the picture from the file.  Downloading a picture is enough
        # A long operation, so in more complex programs it is better
        # do not perform a load every time you redraw the window, like here,
        # and once upload the picture to the property and then use it.
        # For example, you can transfer the loading of pictures to the __init__ method.
        img = QImage ( "grumpycat.jpg" )
        p.drawImage ( QPointF ( 200 , 200 ), img )
        p.drawImage ( QRectF ( 70 , 250 , 50 , 50 ), img )

        # Finish drawing
        p.end ()

def main ():
    app = QApplication ( sys.argv )
    w = MyWidget ()
    w.show ()
    sys.exit ( app . exec_ ())

if __name__ == "__main__" :
    main ()