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
        self.draw_type = 'brush'

        # 3_ Rect
        self.rect_list = []
        self.line_list = []

        # Brush configuration
        self.brush_size = 5
        self.brush_color = Qt.black
        self.last_point = QPoint()
        self.initUI()

    def initUI(self):

        # Menubar setting
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('File')
        setting_menu = menubar.addMenu('Setting')
        draw_menu = menubar.addMenu('Draw')

        # Action #1 : Save
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save)

        # Action #2 : Clear
        clear_action = QAction('Clear', self)
        clear_action.setShortcut('Ctrl+C')
        clear_action.triggered.connect(self.clear)

        # Action #3 : Color
        set_color_action = QAction('Color', self)
        set_color_action.triggered.connect(self.set_color)

        # Mode_Rect :
        mode_rect_action = QAction('Rect', self)
        mode_rect_action.triggered.connect(self.mode_rect)
        # Mode line
        mode_line_action = QAction('line', self)
        mode_line_action.triggered.connect(self.mode_line)


        # Add Action to menu
        filemenu.addAction(save_action)
        filemenu.addAction(clear_action)
        setting_menu.addAction(set_color_action)
        # 2_Rect :
        draw_menu.addAction(mode_rect_action)
        draw_menu.addAction(mode_line_action)


        self.setWindowTitle('Simple Painter')
        self.setGeometry(300, 300, 400, 400)
        self.show()

    # 위젯이 화면에 나타날 때, 자동으로 호출되는 이벤트
    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())
        #painter = QPainter(self.image)

        for line in self.line_list :
            canvas.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            canvas.drawLine(line[0], line[1])

        for rect in self.rect_list :
            canvas.setBrush(self.brush_color)
            canvas.setPen(self.brush_color)            
            canvas.drawRect(rect[0].x(), rect[0].y(), \
                    rect[1].x() - rect[0].x(), rect[1].y()-rect[0].y())        
        
    # 마우스가 클릭될 때 호출되는 이벤트
    def mousePressEvent(self, e):
        # e : event.
        if e.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = e.pos()
            # 2_Rect :
        
        # 3_Rect
        if self.draw_type == 'rect' :
            self.rect_list.append([e.pos(),e.pos()])
            
    # 마우스가 움직일 때 호출되는 이벤트
    def mouseMoveEvent(self, e):
        if (e.buttons() & Qt.LeftButton) & self.drawing and self.draw_type == 'brush':
            self.line_list.append([self.last_point,e.pos()])
            self.last_point = e.pos()
            self.update()
        # 2_Rect :
        
        elif (e.buttons() & Qt.LeftButton) & self.drawing and self.draw_type == 'rect':
            #painter = QPainter(self.image)
            painter = QPainter(self.image)
            
            self.last_point = e.pos()
            self.rect_list[-1][1] = e.pos()
            print(self.rect_list)
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
        self.rect_list = []
        self.line_list = []
        self.update()
        print("clear")

    # Color 기능 메소드
    def set_color(self) :
        new_color = QColorDialog.getColor()
        if new_color.isValid():
            self.brush_color = new_color
    
    def mode_rect(self) :
        self.draw_type = 'rect'

    def mode_line(self) :
        self.draw_type = 'brush'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
