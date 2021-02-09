## Ex 10-5. 간단한 그림판 프로그램.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        # Canvas
        self.image = QImage(QSize(400, 400), QImage.Format_RGB32)
        # Fill Canvas white
        self.image.fill(Qt.white)
        
        # Drawing
        self.drawing = False
        self.brush_size = 5
        self.brush_color = Qt.black
        self.last_point = QPoint()
        self.initUI()

    def initUI(self):

        # Menubar setting
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('File')

        # Action #1 : Save
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save)

        # Action #2 : Clear
        clear_action = QAction('Clear', self)
        clear_action.setShortcut('Ctrl+C')
        clear_action.triggered.connect(self.clear)

        # Add Action to menu
        filemenu.addAction(save_action)
        filemenu.addAction(clear_action)

        self.setWindowTitle('Simple Painter')
        self.setGeometry(300, 300, 400, 400)
        self.show()

    # 위젯이 화면에 나타날 때, 자동으로 호출되는 이벤트
    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())

    # 마우스가 클릭될 때 호출되는 이벤트
    def mousePressEvent(self, e):
        # e : event.
        if e.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = e.pos()

    # 마우스가 움직일 때 호출되는 이벤트
    def mouseMoveEvent(self, e):
        if (e.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(self.last_point, e.pos())
            self.last_point = e.pos()
            self.update()

    # 마우스 클릭이 떼어질 때 호출되는 이벤트
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = False

    # Save 기능 메소드
    def save(self):
        fpath, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if fpath:
            self.image.save(fpath)
    # Clear 기능 메소드
    def clear(self):
        self.image.fill(Qt.white)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
