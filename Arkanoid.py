import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QPlainTextEdit, QSpinBox, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Арканоид')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())