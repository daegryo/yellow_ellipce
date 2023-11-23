import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from des import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor


class Ellipse(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            rr = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            qp.setBrush(QColor(rr, g, b))

            r = random.randint(20, 100)
            x, y = random.randint(0, 800), random.randint(0, 600)
            qp.drawEllipse(int(x - r / 2), int(y - r / 2), r, r)
            # Завершаем рисование
            qp.end()
            self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ellipse()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
