import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow
from random import randint


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.draw)
        self.flag = False

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            color_cir = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            qp.setPen(color_cir)
            qp.setBrush(color_cir)
            r = randint(10, 200)
            x, y = randint(0, 400 - r), randint(0, 400 - r)
            qp.drawEllipse(x, y, r, r)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())
