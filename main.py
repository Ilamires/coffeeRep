import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.CreateYellowEllipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def CreateYellowEllipse(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        f = random.randint(30, 70)
        qp.drawEllipse(random.randint(50, 300), random.randint(50, 300), f, f)
        f = random.randint(30, 70)
        qp.drawEllipse(random.randint(50, 300), random.randint(50, 300), f, f)
        f = random.randint(30, 70)
        qp.drawEllipse(random.randint(50, 300), random.randint(50, 300), f, f)
        f = random.randint(30, 70)
        qp.drawEllipse(random.randint(50, 300), random.randint(50, 300), f, f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
