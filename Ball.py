import math
from PyQt5.QtGui import QColor, QPainter


# Класс шарик
class Ball:
    # радиус шарика
    R = 10

    # # конструктор, принимает координату центра шарика (сx;сy)
    # и угол на который летит шарик
    def __init__(self, cx: float, cy: float, angle: float):
        self.cx = cx
        self.cy = cy
        self.angle = angle

    # рисование шарика
    def draw(self, qp: QPainter):
        # цвет рамки
        pen_color = QColor('black')
        # установка цвета рамки
        qp.setPen(pen_color)
        # цвет кисти шарика
        brush_color = QColor('white')
        # задаем цвет кисти
        qp.setBrush(brush_color)
        # рисуем круг
        qp.drawEllipse(self.cx - Ball.R, self.cy - Ball.R, Ball.R * 2, Ball.R * 2)

    # перемещение шарика
    def move(self):
        # переводим градусы в радианы
        rad = self.angle * math.pi / 180
        # синус - противолежащий катет
        self.cy -= math.sin(rad)
        # косинус - прилежащий катет
        self.cx += math.cos(rad)

    # проверяем, что шарик касается прямоугольника
    def touchedRect(self, x1: int, y1: int, x2: int, y2: int):
        # если коснулся верхней или нижней грани
        if self.touched(x1, y1, x2, y1) or self.touched(x1, y2, x2, y2):
            # то угол отражаем горизонтально
            self.angle = - self.angle
            return True

        # если коснулся левой или правой грани
        if self.touched(x1, y1, x1, y2) or self.touched(x2, y1, x2, y2):
            # то угол отражаем вернтикально
            self.angle = 180 - self.angle
            return True

        # если граней не касаемся,
        # значит не касаемся и прямоугольника
        return False

    # проверяем, что шарик касается
    # отрезка с координатами (x1, y1) и (x2, y2)
    # отрезок может быть только горизонтальный или вертикальный
    def touched(self, x1: int, y1: int, x2: int, y2: int):
        # радиус шарика
        r = Ball.R

        # проверяем, что шарик коснулся первой вершины отрезка
        # по теореме пифагора находим расстояние от центра шарика
        # до вершины, оно должно быть меньше или равно радиуса шарика
        if (x1 - self.cx) ** 2 + (y1 - self.cy) ** 2 <= r ** 2:
            return True

        # аналогично проверяем, что шарик коснулся второй вершины отрезка
        if (x2 - self.cx) ** 2 + (y2 - self.cy) ** 2 <= r ** 2:
            return True

        # если отрезок горизонтальный
        if y1 == y2:
            # проверяем расстояние от центра окружности до отрезка
            if x1 <= self.cx <= x2 and math.fabs(y1 - self.cy) <= r:
                return True
        # иначе отрезок вертикальный
        else:
            if y1 <= self.cy <= y2 and math.fabs(x1 - self.cx) <= r:
                return True

        return False
