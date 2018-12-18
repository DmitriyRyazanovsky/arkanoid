from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QColor, QPainter, QFont


# Класс - надпись на экране
class Label:
    # конструктор, принимает координаты прямоугольника, где будет надпись
    def __init__(self, x: int, y: int, w: int, h: int):
        self.rect = QRectF(x, y, w, h)

    # рисование надписи
    def draw(self, qp: QPainter, text: str):
        # цвет рамки и текста
        pen_color = QColor('red')
        # задаем цвет рамки и текста
        qp.setPen(pen_color)
        # цвет фона
        brush_color = QColor('white')
        # задаем цвет фона
        qp.setBrush(brush_color)
        # рисуем рамку
        qp.drawRect(self.rect)
        # задаем шрифт
        qp.setFont(QFont('Arial', 12))
        # пишем надпись в прямоугольнике с выравниванием по центу
        qp.drawText(self.rect, Qt.AlignCenter, text + "\nНажмите пробел для продолжения")
