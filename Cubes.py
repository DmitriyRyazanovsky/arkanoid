from PyQt5.QtGui import QPainter

from Cube import Cube


# Класс кубики - список кубиков
class Cubes(list):
    def __init__(self):
        # вызов конструктора базового класса
        super().__init__()
        # уровень
        self.level = 1

    # заполнение кубиков
    def initCubes(self):
        # предварительно всё очищаем
        self.clear()
        # координата y кубиков
        y = 50
        # рядов столько же, сколько цветов в радуге
        for row in range(len(Cube.RAINBOW) - self.level, len(Cube.RAINBOW)):
            # координата x кубиков
            x = 53
            # 11 кубиков в ряду
            for col in range(0, 11):
                # создание кубика
                cube = Cube(x, y, row)
                # добавляем кубик
                self.append(cube)
                # увеличиваем коородинату x кубиков
                x += Cube.W + 2
            # увеличиваем коородинату y кубиков
            y += Cube.H + 2

    # рисование кубиков
    def draw(self, qp: QPainter):
        # пробегаемся по всем кубикам
        for cube in self:
            # и рисуем каждый кубик
            cube.draw(qp)
