import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.label1 = QLabel('점수1:', self)
        self.label2 = QLabel('점수2:', self)
        self.label3 = QLabel('결과:', self) #Hello..
        self.line_edit1 = QLineEdit(self)
        self.line_edit2 = QLineEdit(self)
        self.text_edit = QTextEdit(self)
        self.trans_btn = QPushButton('번역', self)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.line_edit1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.line_edit2)

        vbox.addWidget(self.label3)
        vbox.addWidget(self.text_edit)
        vbox.addWidget(self.trans_btn)
        self.setLayout(vbox)

        self.trans_btn.clicked.connect(self.get_result)
        #self.line_edit1.editingFinished.connect(self.translate_kor)

        self.setWindowTitle('Google Translator')
        self.setGeometry(200, 200, 400, 300)
        self.show()

    def get_result(self):
        try :
            result = int(self.line_edit1.text()) + int(self.line_edit2.text())
        except ValueError as e:
            self.text_edit.setText(str(type(e)))
            return
        self.text_edit.setText(str(result))
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())