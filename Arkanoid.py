import math
import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont

from Cubes import Cubes
from Cube import Cube
from Ball import Ball
from Racket import Racket

W = 800
H = 600

STATE_PAUSE = 1
STATE_RUN = 2
STATE_WIN = 3
STATE_LOSE = 4


class Arkanoid(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, W, H)
        self.setWindowTitle('Арканоид')

        self.cubes = Cubes()
        self.racket = Racket(W / 2 - Racket.W / 2)
        self.ball = Ball(W / 2, Racket.Y - Ball.R, 60)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.time)
        self.timer.start(1)

        self.setMouseTracking(1)

        self.state = STATE_PAUSE

    def paintEvent(self, e):
        try:
            qp = QPainter()
            qp.begin(self)
            self.cubes.draw(qp)
            self.racket.draw(qp)
            self.ball.draw(qp)
            self.drawState(qp)
            qp.end()
        except Exception as e:
            print(e)

    def drawState(self, qp: QPainter):
        if (self.state == STATE_PAUSE):
            qp.setPen(QColor('red'))
            qp.setPen(QColor('red'))
            qp.drawRect(290, 280, 217, 40)
            qp.setFont(QFont('Decorative', 10))
            qp.drawText(QtCore.QRectF(0, 0, W, H), QtCore.Qt.AlignCenter, "Нажмите пробел для продолжения")

    def keyPressEvent(self, event):
        if self.state == STATE_RUN:
            if event.key() == 16777234:  # Left
                self.racket.x -= 20
            elif event.key() == 16777236:  # Right
                self.racket.x += 20
            if self.racket.x <= 1:
                self.racket.x = 1
            if self.racket.x + Racket.W >= W:
                self.racket.x = W - Racket.W
            if event.key() == 32:  # Space
                self.state = STATE_PAUSE
            self.update()
        elif self.state == STATE_PAUSE:
            if event.key() == 32:  # Space
                self.state = STATE_RUN

    def mouseMoveEvent(self, event):
        if self.state == STATE_RUN:
            newX = event.pos().x() - Racket.W / 2
            if newX != self.racket.x:
                self.racket.x = newX
                self.update()

    def time(self):
        try:
            if self.state != STATE_RUN:
                return

            rad = self.ball.alfa * math.pi / 180
            self.ball.cy -= math.sin(rad)
            self.ball.cx += math.cos(rad)

            # screen right
            if self.ball.touched(W, 0, W, H):
                self.ball.alfa = 180 - self.ball.alfa

            # screen top
            if self.ball.touched(0, 0, W, 0):
                self.ball.alfa = - self.ball.alfa

            # screen left
            if self.ball.touched(0, 0, 0, H):
                self.ball.alfa = 180 - self.ball.alfa

            left = int(self.ball.cx - Ball.R)
            right = int(self.ball.cx + Ball.R)
            bottom = int(self.ball.cy + Ball.R)
            top = int(self.ball.cy - Ball.R)

            # rocket top
            if self.ball.touched(self.racket.x, Racket.Y, self.racket.x + Racket.W, Racket.Y):
                self.ball.alfa = - self.ball.alfa

            for cube in self.cubes:
                inCube = False

                # cube bottom
                if self.ball.touched(cube.x, cube.y + Cube.H, cube.x + Cube.W, cube.y + Cube.H):
                    self.ball.alfa = - self.ball.alfa
                    inCube = True

                # cube top
                if self.ball.touched(cube.x, cube.y, cube.x + Cube.W, cube.y + Cube.H):
                    self.ball.alfa = - self.ball.alfa
                    inCube = True

                # cube left
                if self.ball.touched(cube.x, cube.y, cube.x, cube.y + Cube.H):
                    self.ball.alfa = 180 - self.ball.alfa
                    inCube = True

                # cube right
                if self.ball.touched(cube.x + Cube.W, cube.y, cube.x + Cube.W, cube.y + Cube.H):
                    self.ball.alfa = 180 - self.ball.alfa
                    inCube = True

                if inCube:
                    cube.collorNumber += 1
                    if cube.collorNumber >= len(Cube.COLOR):
                        self.cubes.remove(cube)

            self.update()

        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    arkanoid = Arkanoid()
    arkanoid.show()
    sys.exit(app.exec())
