import math
from PyQt5.QtGui import QColor, QPainter


class Ball:
    R = 10

    def __init__(self, cx : float, cy : float, alfa : float):
        self.cx = cx
        self.cy = cy
        self.alfa = alfa

    def draw(self, qp: QPainter):
        brushCollor = QColor('white')
        qp.setBrush(brushCollor)
        qp.drawEllipse(self.cx - Ball.R, self.cy - Ball.R, Ball.R * 2, Ball.R * 2)

    def touched(self, x1, y1, x2, y2):
        if (x1 - self.cx) ** 2 + (y1 - self.cy) ** 2 <= Ball.R ** 2:
            return True

        if (x2 - self.cx) ** 2 + (y2 - self.cy) ** 2 <= Ball.R ** 2:
            return True

        if y1 == y2:
            if x1 <= self.cx <= x2 and math.fabs(y1 - self.cy) <= Ball.R:
                return True
        else:
            if y1 <= self.cy <= y2 and math.fabs(x1 - self.cx) <= Ball.R:
                return True

        return False