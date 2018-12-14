from PyQt5.QtGui import QPainter

from Cube import Cube


class Cubes(list):
    def __init__(self):
        for x in range(1, 15):
            for y in range(0, len(Cube.COLOR)):
                cube = Cube(x * 53 - 20, (y + 1) * 23, y)
                self.append(cube)

    def draw(self, qp: QPainter):
        for cube in self:
            cube.draw(qp)
