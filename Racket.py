from PyQt5.QtGui import QPainter, QColor


# Класс - ракетка
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
    def __init__(self, x: int):
        self.x = x

    # рисование ракетки
    def draw(self, qp: QPainter):
        # цвет рамки
        pen_color = QColor('black')
        # установка цвета рамки
        qp.setPen(pen_color)
        # цвет кисти ракетки
        brush_color = QColor('lightGray')
        # задаем цвет ракетки
        qp.setBrush(brush_color)
        # рисуем ракетку
        qp.drawRect(self.x + 10, Racket.Y, Racket.W - 20, Racket.H)

        # цвет углов ракетки
        brush_color = QColor('red')
        # задаем цвет кисти
        qp.setBrush(brush_color)
        # рисуем левый угол ракетки
        qp.drawRect(self.x, Racket.Y, 10, Racket.H)
        # рисуем правый угол ракетки
        qp.drawRect(self.x + Racket.W - 10, Racket.Y, 10, Racket.H)

        # центр ракетки по горизонтали
        x = self.x + Racket.W / 2

        # рисование вертикальной линии по центру ракетки
        # показывающей, что в случае удара по центру
        # шарик полетит вверх
        qp.drawLine(x, Racket.Y, x, Racket.Y + Racket.H)

        # рисование наклонных линий показывающих,
        # что в случае удара сбоку, шарик полетит вбок
        qp.drawLine(x - 40, Racket.Y, x - 40 + Racket.H, Racket.Y + Racket.H)
        qp.drawLine(x - 80, Racket.Y, x - 80 + Racket.H * 2, Racket.Y + Racket.H)
        qp.drawLine(x + 40, Racket.Y, x + 40 - Racket.H, Racket.Y + Racket.H)
        qp.drawLine(x + 80, Racket.Y, x + 80 - Racket.H * 2, Racket.Y + Racket.H)
