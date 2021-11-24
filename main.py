import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()

        self.result = cur.execute("""SELECT varieties,roast,groundORInGrains,taste,price,volume
                                    FROM coffees""").fetchall()
        self.page = 1
        self.pages = len(self.result) // 5 + 1
        print(self.result)
        self.Change()
        con.close()

    def ChangePage(self):
        if self.sender().text() == '>' and self.page < self.pages:
            self.page += 1
        elif self.page > 1:
            self.page -= 1
        self.Change()

    def Change(self):
        for i in range(5):
            if i + (self.page - 1) * 5 <= len(self.result) - 1:
                eval(f"self.lbl1_{i + 1 + (self.page - 1) * 5}.setText('{self.result[i][0]}')")
                eval(f"self.lbl2_{i + 1 + (self.page - 1) * 5}.setText('{self.result[i][1]}')")
                eval(f"self.lbl3_{i + 1 + (self.page - 1) * 5}.setText('{self.result[i][2]}')")
                eval(f"self.lbl4_{i + 1 + (self.page - 1) * 5}.setText('{self.result[i][3]}')")
                eval(f"self.lbl5_{i + 1 + (self.page - 1) * 5}.setText('{self.result[i][4]}')")
                eval(f"self.lbl6_{i + 1 + (self.page - 1) * 5}.setText('{self.result[i][5]}')")
            else:
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
