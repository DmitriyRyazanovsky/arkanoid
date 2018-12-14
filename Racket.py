from PyQt5.QtGui import QPainter, QColor


class Racket:
    W = 200
    H = 10
    Y = 540

    def __init__(self, x):
        self.x = x

    def draw(self, qp: QPainter):
        brushCollor = QColor('lightGray')
        qp.setBrush(brushCollor)
        qp.drawRect(self.x, Racket.Y, Racket.W, Racket.H)
