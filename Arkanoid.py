import math
import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont

from Year2.arkanoid import Cube

R = 10
W = 800
H = 600
RACKET_Y = 550
RACKET_W = 100
SPEED = 1

STATE_PAUSE = 1
STATE_RUN = 2
STATE_WIN = 3
STATE_LOSE = 4


class Arkanoid(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initCubes()

    def initUI(self):
        self.setGeometry(300, 300, W, H)
        self.setWindowTitle('Арканоид')

        self.racketX = W / 2 - RACKET_W / 2
        self.ballX = W / 2
        self.ballY = RACKET_Y - R
        self.a = 30
        self.racketY = RACKET_Y

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.time)
        self.timer.start(1)

        self.setMouseTracking(1)

        self.state = STATE_PAUSE

    def initCubes(self):
        self.cubes = []
        for x in range(1, 15):
            for y in range(0, len(Cube.COLOR)):
                cube = Cube(x * 53 - 20, (y + 1) * 23, y)
                self.cubes.append(cube)

    def paintEvent(self, e):
        try:
            qp = QPainter()
            qp.begin(self)
            self.drawCubes(qp)
            self.drawRacket(qp)
            self.drawBall(qp)
            self.drawState(qp)
            qp.end()
        except Exception as e:
            print(e)

    def drawCubes(self, qp):
        for cube in self.cubes:
            cube.draw(qp)

    def drawRacket(self, qp):
        brushCollor = QColor('lightGray')
        qp.setBrush(brushCollor)
        qp.drawRect(self.racketX, self.racketY, RACKET_W, 10)

    def drawBall(self, qp: QPainter):
        brushCollor = QColor('white')
        qp.setBrush(brushCollor)
        qp.drawEllipse(self.ballX - R, self.ballY - R, R * 2, R * 2)

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
                self.racketX -= 20
            elif event.key() == 16777236:  # Right
                self.racketX += 20
            if self.racketX <= 1:
                self.racketX = 1
            if self.racketX + RACKET_W >= W:
                self.racketX = W - RACKET_W
            if event.key() == 32:  # Space
                self.state = STATE_PAUSE
            self.update()
        elif self.state == STATE_PAUSE:
            if event.key() == 32:  # Space
                self.state = STATE_RUN

    def mouseMoveEvent(self, event):
        if self.state == STATE_RUN:
            newX = event.pos().x() - RACKET_W / 2
            if newX != self.racketX:
                self.racketX = newX
                self.update()

    def time(self):
        try:
            if self.state != STATE_RUN:
                return

            rad = self.a * math.pi / 180
            self.ballY -= math.sin(rad) * SPEED
            self.ballX += math.cos(rad) * SPEED

            # screen right
            if self.touched(W, 0, W, H):
                self.a = 180 - self.a

            # screen top
            if self.touched(0, 0, W, 0):
                self.a = - self.a

            # screen left
            if self.touched(0, 0, 0, H):
                self.a = 180 - self.a

            left = int(self.ballX - R)
            right = int(self.ballX + R)
            bottom = int(self.ballY + R)
            top = int(self.ballY - R)

            # rocket top
            if self.touched(self.racketX, self.racketY, self.racketX + RACKET_W, self.racketY):
                self.a = - self.a

            for cube in self.cubes:
                inCube = False

                # cube bottom
                if self.touched(cube.x, cube.y + cube.h, cube.x + cube.w, cube.y + cube.h):
                    self.a = - self.a
                    inCube = True

                # cube top
                if self.touched(cube.x, cube.y, cube.x + cube.w, cube.y + cube.h):
                    self.a = - self.a
                    inCube = True

                # cube left
                if self.touched(cube.x, cube.y, cube.x, cube.y + cube.h):
                    self.a = 180 - self.a
                    inCube = True

                # cube right
                if self.touched(cube.x + cube.w, cube.y, cube.x + cube.w, cube.y + cube.h):
                    self.a = 180 - self.a
                    inCube = True

                if inCube:
                    cube.collor += 1
                    if cube.collor >= len(COLOR):
                        self.cubes.remove(cube)

            self.update()

        except Exception as e:
            print(e)

    def touched(self, x1, y1, x2, y2):
        if (x1 - self.ballX) ** 2 + (y1 - self.ballY) ** 2 <= R ** 2:
            return True
        if (x2 - self.ballX) ** 2 + (y2 - self.ballY) ** 2 <= R ** 2:
            return True
        if y1 == y2:
            if x1 <= self.ballX <= x2 and math.fabs(y1 - self.ballY) <= R:
                return True
        else:
            if y1 <= self.ballY <= y2 and math.fabs(x1 - self.ballX) <= R:
                return True
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    arkanoid = Arkanoid()
    arkanoid.show()
    sys.exit(app.exec())
