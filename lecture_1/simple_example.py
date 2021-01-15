import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.label1 = QLabel('Test Label:', self)
        self.btn = QPushButton('확인', self)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)
        self.setWindowTitle('First PyQt App')
        self.setGeometry(200, 200, 400, 300)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())