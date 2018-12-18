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
    def __init__(self, x: int, y: int, collor_number: int):
        self.x = x
        self.y = y
        self.collor_number = collor_number

    # рисование кубика
    def draw(self, qp: QPainter):
        # цвет рамки
        pen_color = QColor('black')
        # установка цвета рамки
        qp.setPen(pen_color)
        # цвет кисти
        brush_color = QColor(Cube.RAINBOW[self.collor_number])
        # установка кисти
        qp.setBrush(brush_color)
        # рисование прямоугольника
        qp.drawRect(self.x, self.y, Cube.W, Cube.H)

        # цвет светлых полос внутри кубика
        pen_color = QColor('white')
        # установка цвета линии
        qp.setPen(pen_color)
        # рисование верхней светлой полосы внутри кубика
        qp.drawLine(self.x + 1, self.y + 1, self.x + Cube.W - 1, self.y + 1)
        # рисование левой светлой полосы внутри кубика
        qp.drawLine(self.x + 1, self.y + 1, self.x + 1, self.y + Cube.H - 1)

        # цвет темных полос внутри кубика
        pen_color = QColor('gray')
        # установка цвета линии
        qp.setPen(pen_color)
        # рисование нижней темной полосы внутри кубика
        qp.drawLine(self.x + 2, self.y + Cube.H - 1, self.x + Cube.W - 1, self.y + Cube.H - 1)
        # рисование правой темной полосы внутри кубика
        qp.drawLine(self.x + Cube.W - 1, self.y + 1, self.x + Cube.W - 1, self.y + Cube.H - 1)
