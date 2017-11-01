import sys
from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QSpinBox
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QTimer
from math import sin, cos, pi


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.process_timeout)
        self.timer.start(16)  # 16 - period in milliseconds
        self.phi = 0  # Angle in radians.
        self.speed = 0.01  # How much does self.phi change for
                           # one countdown timer.
        self.resize(600, 500)
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(500, 50)
        self.slider.setValue(0.01)
        self.slider.valueChanged.connect(self.change_rotation_speed)
        self.spinbox = QSpinBox(self)
        self.spinbox.move(500, 100)
        self.n = 4
        self.spinbox.setValue(self.n)
        self.spinbox.valueChanged.connect(self.change_number_of_angles)

    def process_timeout(self):
        self.phi += self.speed
        self.update()

    def change_number_of_angles(self, new_n):
        self.n = new_n

    def change_rotation_speed(self, new_speed):
        print(new_speed)
        self.speed = 0.1 * new_speed / 100

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        pen = QPen(Qt.red, 10)
        p.setPen(pen)

        centerx, centery = 250, 250
        n = self.n
        for i in range(n):
            angle = self.phi + pi / n + ((2 * pi) / n) * i
            p.drawPoint(centerx + 200 * cos(angle),
                        centery + 200 * sin(angle))

        p.end()


def main():
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()