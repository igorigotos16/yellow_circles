import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        
        self.btn.clicked.connect(self.draw)

        self.flag = False

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            qp.setBrush(QColor(255, 255, 0))
            r = randint(10, 200)
            x, y = randint(0, 400 - r), randint(0, 400 - r)
            qp.drawEllipse(x, y, r, r)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
