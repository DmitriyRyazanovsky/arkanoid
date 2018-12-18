from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QColor, QPainter, QFont


# Класс - количество очков
class Scores:
    # конструктор, принимает координаты прямоугольника, где будут отображаться очки
    def __init__(self, x: int, y: int, w: int, h: int):
        self.rect = QRectF(x, y, w, h)
        self.count = 0

    # рисование надписи
    def draw(self, qp: QPainter):
        # цвет цифр
        pen_сolor = QColor('blue')
        # задаем цвет цифр
        qp.setPen(pen_сolor)
        # задаем шрифт
        qp.setFont(QFont('Arial', 16))
        # пишем количество очков с выравниванием по правому краю
        qp.drawText(self.rect, Qt.AlignCenter, str(self.count))
