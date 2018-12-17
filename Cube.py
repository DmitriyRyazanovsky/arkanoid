from PyQt5.QtGui import QColor, QPainter


# Класс Кубик
class Cube:
    # цвета радуги, в которые раскрашиваются кубики в каждом ряде
    RAINBOW = ['red', 'orange', 'yellow', 'green', 'aqua', 'blue', 'purple']
    # ширина кубика
    W = 60
    # высота кубика
    H = 22

    # конструктор, принимает координату левого верхнего угла кубика (x;y) и номер цвета
    def __init__(self, x: int, y: int, collorNumber: int):
        self.x = x
        self.y = y
        self.collorNumber = collorNumber

    # рисование кубика
    def draw(self, qp: QPainter):
        # цвет кисти
        brushColor = QColor(Cube.RAINBOW[self.collorNumber])
        # установка кисти
        qp.setBrush(brushColor)
        # рисование прямоугольника
        qp.drawRect(self.x, self.y, Cube.W, Cube.H)
