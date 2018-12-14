from PyQt5.QtGui import QColor, QPainter

COLOR = ['red', 'orange', 'yellow', 'green', 'aqua', 'blue', 'purple']
W = 50
H = 20

class Cube:
    def __init__(self, x : int, y : int, collorNumber : int):
        self.x = x
        self.y = y
        self.collorNumber = collorNumber

    def draw(self, qp : QPainter):
        qp.setPen(QColor('black'))
        brushColor = QColor(COLOR[self.collorNumber])
        qp.setBrush(brushColor)
        qp.drawRect(self.x, self.y, W, H)
