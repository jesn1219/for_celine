import sys
from PyQt5.QtWidgets import *


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        # 위젯 생성
        self.label_1 = QLabel('라벨:', self)
        self.button = QPushButton('버튼', self)

        # 위젯들을 레이아웃에 배치
        vertical_box_layout = QVBoxLayout() #Vertical Box 레이아웃 사용

        # 차례대로 추가됨.. Vertical 방향으로!
        vertical_box_layout.addWidget(self.label_1)
        vertical_box_layout.addWidget(self.button)

        # self(가장 큰 위젯)의 레이아웃을, 위에서 설정한 vertical_box_layout으로 설정
        self.setLayout(vertical_box_layout)

        # 윈도우 창 조절
        self.setWindowTitle('Inital format file')
        self.move(200, 200)
        self.resize(300,200)

        # Show widget in screen
        self.show()
        

  

# __name__ : Current Moudule's name
# __main__ : if this code excuted directly, __name__ is __main__
if __name__ == '__main__':
    # Create App object
    app = QApplication(sys.argv)
    
    # Create Widget
    ex = MyWidget()
    
    # If, Widget is closed, Exit Program
    sys.exit(app.exec_())