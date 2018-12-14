from PyQt5.QtGui import QColor, QPainter


class Cube:
    COLOR = ['red', 'orange', 'yellow', 'green', 'aqua', 'blue', 'purple']
    W = 50
    H = 20

    def __init__(self, x: int, y: int, collorNumber: int):
        self.x = x
        self.y = y
        self.collorNumber = collorNumber

    def draw(self, qp: QPainter):
        brushColor = QColor(Cube.COLOR[self.collorNumber])
        qp.setBrush(brushColor)
        qp.drawRect(self.x, self.y, Cube.W, Cube.H)
