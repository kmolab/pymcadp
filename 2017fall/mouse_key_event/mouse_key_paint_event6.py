import sys
from PyQt5.QtWidgets import (
QWidget , QApplication , QSlider , QSpinBox ,
QLabel , QCheckBox , QPushButton
)
from PyQt5.QtGui import QPainter , QPen
from PyQt5.QtCore import Qt , QTimer

class MyWidget ( QWidget ):
    def __init__ ( self ):
        super ().__init__ ()
        self.button = QPushButton ( self )
        self.button.setText ( 'Push me!' )
        self.button.move ( 100 , 100 )
        # We connect the button click handler.
        self.button.clicked.connect (
        self.button_clicked
        )

        self.slider = QSlider ( Qt.Horizontal , self )
        self.slider.move ( 100 , 150 )
        # Connect the handler of the new values ​​of the slider
        self.slider.valueChanged.connect (
        self.slider_moved
        )

        self.label = QLabel ( self )
        self.label.move ( 100 , 200 )

        self.checkbox = QCheckBox ( self )
        self.checkbox.move ( 100 , 250 )
        self.checkbox.setText ( 'Check me!' )
        # Connect the handler of the new values ​​of the slider
        self.checkbox.stateChanged.connect (
        self.checkbox_changed
        )

    def checkbox_changed ( self , new_state ):
        # A method that responds to a change in the state of the checkbox.
        if new_state :
            self.label.setText ( 'Ok' )
        else :
            self.label.setText ( 'Fail' )
        # Change the size of the label so that the text is placed.
        # In the future, we will use the layout managers,
        # which it will do automatically.
        self.label.resize ( self . label . sizeHint ())

    def button_clicked ( self ):
        # A method that responds to a button click.
        print ( 'Hello, world!' )
        self.label.setText (
        'slider:' + str ( self . slider . value ()) +
        'checkbox:' + str ( self . checkbox . checkState ())
        )
        self.label.resize ( self . label . sizeHint ())

    def slider_moved ( self , new_value ):
        # A method that responds to the movement of the slider.
        self.label.setText ( str ( new_value ))
        self.label.resize ( self . label . sizeHint ())


def main ():
    app = QApplication ( sys.argv )
    w = MyWidget ()
    w.show ()
    sys.exit ( app . exec_ ())

if __name__ == "__main__" :
    main ()