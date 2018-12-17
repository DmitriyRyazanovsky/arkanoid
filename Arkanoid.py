import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter

from Cubes import Cubes
from Cube import Cube
from Ball import Ball
from Racket import Racket
from Label import Label
from Scores import Scores

# состояние - запуск
STATE_START = 1
# состояние - пауза
STATE_PAUSE = 2
# состояние - игра
STATE_GAME = 3
# состояние - выигрыш
STATE_WIN = 4
# состояние - проигрыш
STATE_LOSE = 5

# код класиши Влево
KEY_LEFT = 16777234
# код класиши Вправо
KEY_RIGHT = 16777236
# код класиши Пробел
KEY_SPACE = 32


# Класс - Арканоид - основное поле игры
class Arkanoid(QWidget):
    # ширина поля
    W = 800
    # высота поля
    H = 600

    # конструктор
    def __init__(self):
        super().__init__()
        self.initUI()

    # подготовка поля
    def initUI(self):
        # перемещение
        self.move(300, 300)
        # фиксируем ширину и высоту поля
        self.setFixedSize(Arkanoid.W, Arkanoid.H)
        # задаём имя программы
        self.setWindowTitle('Арканоид')

        # создаём кубики
        self.cubes = Cubes()
        # созаём ракетку
        self.racket = Racket(Arkanoid.W / 2 - Racket.W / 2)
        # создаём шарик
        self.ball = Ball(Arkanoid.W / 2, Racket.Y - Ball.R, 60)
        # создаём надпись
        self.label = Label(150, Arkanoid.H / 2, Arkanoid.W - 300, 60)
        # создаем очки
        self.scores = Scores(0, 9, Arkanoid.W, 30)

        # создаём таймер
        self.timer = QtCore.QTimer()
        # заканчиваем время
        self.timer.timeout.connect(self.tick)
        # задаём начало счётчика
        self.timer.start(1)

        # включаем отслеживание мыши
        self.setMouseTracking(1)
        # переходим в состояние запуска
        self.start()

    # запуск арканоида
    def start(self):
        # заполняем кубики
        self.cubes.initCubes()
        # сбрасываем очки
        self.scores = 0
        # сбрасываем позицию и угол шарика
        self.ball.cx = Arkanoid.W / 2
        self.ball.cy = Racket.Y - Ball.R
        self.ball.alfa = 60
        # переходим в состояние запуска
        self.state = STATE_START

    # перекрытие функции рисования на окне
    def paintEvent(self, e):
        # обработка ошибок
        try:
            # создаём рисовальщик
            qp = QPainter()
            # начало рисования
            qp.begin(self)
            # рисуем кубики
            self.cubes.draw(qp)
            # рисуем ракетку
            self.racket.draw(qp)
            # рисуем шарик
            self.ball.draw(qp)
            # рисуем надпись
            self.drawState(qp)
            # рисуем очки
            self.scores.draw(qp)
            # завершение рисования
            qp.end()
        except Exception as e:
            # печать ошибок
            print(e)

    # взависимости от текущего состояния
    # выводим на экран ту или иную запись
    def drawState(self, qp: QPainter):
        if (self.state == STATE_START):
            self.label.draw(qp, "Добро пожаловать в Арканоид!")
        elif (self.state == STATE_PAUSE):
            self.label.draw(qp, "Пауза")
        elif (self.state == STATE_WIN):
            self.label.draw(qp, "Вы выиграли! Поздравляю!")
        elif (self.state == STATE_LOSE):
            self.label.draw(qp, "Вы проиграли")

    # обработка клавиатуры
    def keyPressEvent(self, event):
        if self.state == STATE_GAME:
            # если во время игры нажали Влево
            if event.key() == KEY_LEFT:
                # то смещаем рокетку Влево
                self.moveRocketTo(self.racket.x - Racket.DX)
            # если во время игры нажали Вправо
            elif event.key() == KEY_RIGHT:
                #  то смещаем ракетку Вправо
                self.moveRacketTo(self.racket.x + Racket.DX)
            # если во время игры нажали Пробел
            if event.key() == KEY_SPACE:
                #  то переходим в сотояние паузы
                self.state = STATE_PAUSE
                # обновляем окно
                self.update()
        else:
            # если нажат Пробел
            if event.key() == KEY_SPACE:
                #  переходим в состояние игры
                self.state = STATE_GAME
                # обновляем окно
                self.update()

    # обработка перемещения мыши
    def mouseMoveEvent(self, event):
        # если во время игры перемещаем мышь
        if self.state == STATE_GAME:
            # то перемещаем ракетку
            self.moveRacketTo(event.pos().x() - Racket.W / 2)

    # перемещение ракетки
    def moveRacketTo(self, x: int):
        # ракетку нельзя выводить за левый край экрана
        if x < 1:
            x = 1

        # ракетку нельзя выводить за правый край экрана
        if x + Racket.W >= Arkanoid.W - 2:
            x = Arkanoid.W - 2 - Racket.W

        # если позиция ракетки изменилась
        if self.racket.x != x:
            # то перемещаем ракетку
            self.racket.x = x
            # обновляем экран
            self.update()

    # обработчик таймера
    def tick(self):
        try:
            # если не в состоянии игры, то таймер игнорируем
            if self.state != STATE_GAME:
                return

            # перемещение шарика
            self.ball.move()

            # обработка касания шариком краев экрана
            self.ball.touchedRect(0, 0, Arkanoid.W, Arkanoid.H)

            # обработка касания шариком ракетки
            self.ball.touchedRect(self.racket.x, Racket.Y, self.racket.x + Racket.W, Racket.Y + Racket.H)

            # обработка касания шариком кубиков
            for cube in self.cubes:
                # если мяч коснулся куба
                if self.ball.touchedRect(cube.x, cube.y, cube.x + Cube.W, cube.y + Cube.H):
                    # изменение номера цвета куба
                    cube.collorNumber += 1
                    self.scores.count += 1
                    # если цвет куба больше количества цветов
                    if cube.collorNumber >= len(Cube.RAINBOW):
                        # убираем кубик
                        self.cubes.remove(cube)

            # если мяч ниже поля
            if self.ball.cy > Arkanoid.H:
                # переходим в состояние пройгрыша
                self.state = STATE_LOSE

            # если кубики закончились
            if len(self.cubes) == 0:
                # переходим в состояние выйгрыша
                self.state = STATE_WIN

            # обновляем экран
            self.update()

        except Exception as e:
            # печать ошибок
            print(e)


# создание и отображение окна программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    arkanoid = Arkanoid()
    arkanoid.show()
    sys.exit(app.exec())
