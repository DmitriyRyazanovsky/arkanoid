from PyQt5.QtGui import QPainter, QColor


# класс ракетка
class Racket:
    # ширина ракетки
    W = 200
    # высота
    H = 12
    # положение по Y
    Y = 540
    # смещение ракетки
    DX = 20

    # конструктор, принимает положение по X
    def __init__(self, x):
        self.x = x

    # рисование ракетки
    def draw(self, qp: QPainter):
        # цвет кисти ракетки
        brushCollor = QColor('lightGray')
        # задаем цвет ракетки
        qp.setBrush(brushCollor)
        # рисуем ракетку
        qp.drawRect(self.x, Racket.Y, Racket.W, Racket.H)
