import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Арканоид')

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        self.drawRacket(qp)
        self.drawBall(qp)
        qp.end()

    def drawRectangles(self, qp):
        Color = ['red', 'orange', 'yellow', 'green', 'aqua', 'blue', 'purple']
        penColor = QColor(0, 0, 0)
        brushCollor = QColor(0, 0, 0)
        for x in range(1, 15):
            for y in range(0, len(Color)):
                #penColor.setNamedColor(Color[y])
                qp.setPen(penColor)
                brushCollor.setNamedColor(Color[y])
                qp.setBrush(brushCollor)
                qp.drawRect(x * 53 - 20, (y+1) * 23, 50, 20)

    def drawRacket(self,qp):
        brushCollor = QColor('lightGray')
        qp.setBrush(brushCollor)
        qp.drawRect(340,550,120,10)

    def drawBall(self, qp : QPainter):
        brushCollor = QColor('white')
        qp.setBrush(brushCollor)
        qp.drawEllipse(390, 530, 20, 20)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
