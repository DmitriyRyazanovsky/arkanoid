from PyQt5.QtGui import QPainter

from Cube import Cube


# Класс кубики - список кубиков
class Cubes(list):
    # заполнение кубиков
    def initCubes(self):
        # предварительно всё очищаем
        self.clear()
        # 11 кубиков в ряду
        for x in range(0, 11):
            # рядов столько же, сколько цветов в радуге
            for y in range(0, len(Cube.RAINBOW)):
                # создание кубика
                cube = Cube((x + 1) * (Cube.W + 2) - 3, (y + 1) * (Cube.H + 2) + 25, y)
                # добавляем кубик
                self.append(cube)

    # рисование кубиков
    def draw(self, qp: QPainter):
        # пробегаемся по всем кубикам
        for cube in self:
            # и рисуем каждый кубик
            cube.draw(qp)
