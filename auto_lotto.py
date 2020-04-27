# auto_lotto.py
import random
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QHBoxLayout, QVBoxLayout, QTextBrowser, \
    QLineEdit, QLabel
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label1 = QLabel('횟수 입력: ', self)

        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label1, 0)
        hbox.addWidget(self.le, 1)
        hbox.addStretch(1)

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox)
        vbox1.addWidget(self.tb, 1)
        vbox1.addWidget(self.clear_btn, 2)

        self.setLayout(vbox1)

        self.setWindowIcon(QIcon('D:\Python\Mymodules\\auto_lotto\\favicon.png'))
        # self.setGeometry(800, 800, 800, 600)
        self.setWindowTitle("로또 번호 자동 추첨 프로그램 by SteveKwon211")
        self.resize(800, 550)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def append_text(self):
        self.autolotto()
        self.le.clear()

    def clear_text(self):
        self.tb.clear()

    def autolotto(self):
        num = self.le.text()

        for i in range(int(num)):
            ballnum = [x + 1 for x in range(45)]
            result = []

            for j in range(6):
                random.shuffle(ballnum)
                nums = ballnum.pop()
                result.append(nums)
                result.sort()

            self.tb.append(time.strftime('%x', time.localtime(time.time())) + '\n' + "로또 번호 [%d]\n" % (i + 1) + str(
                result[0:]) + '\n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

a = MyApp()
