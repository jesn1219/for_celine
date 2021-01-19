import sys
from PyQt5.QtWidgets import *


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        # 위젯 생성
        self.score_label_1 = QLabel('점수1:', self)
        self.score_label_2 = QLabel('점수2:', self)
        self.result_label = QLabel('결과:', self) 
        self.score_edit_1 = QLineEdit(self)
        self.score_edit_2 = QTextEdit(self)
        self.result_edit = QLineEdit(self)
        self.calcul_btn = QPushButton('계산', self)


        # 위젯들을 레이아웃에 배치
        vertical_box_layout = QVBoxLayout() #Vertical Box 레이아웃 사용

        # 차례대로 추가됨.. Vertical 방향으로!
        vertical_box_layout.addWidget(self.score_label_1)
        vertical_box_layout.addWidget(self.score_edit_1)
        vertical_box_layout.addWidget(self.score_label_2)
        vertical_box_layout.addWidget(self.score_edit_2)
        vertical_box_layout.addWidget(self.result_label)
        vertical_box_layout.addWidget(self.result_edit)
        vertical_box_layout.addWidget(self.calcul_btn)

        # self(가장 큰 위젯)의 레이아웃을, 위에서 설정한 vertical_box_layout으로 설정
        self.setLayout(vertical_box_layout)

        # 버튼에 기능 추가. calcul_btn을 누르면, self.get_result 함수가 실행됨
        self.calcul_btn.clicked.connect(self.get_result)


        self.setWindowTitle('Inital format file')
        self.move(200, 200)
        self.resize(300,200)
        # Same as :
        #self.setGeometry(0, 0, 600, 600)
    
        # Show widget in screen
        self.show()
        
    def get_result(self):
        
        # 결과 계산
        result = 0.5 * ( int(self.score_edit_1.text()) + int(self.score_edit_2.text()) )
        self.result_edit.setText(str(result))
        

  

# __name__ : Current Moudule's name
# __main__ : if this code excuted directly, __name__ is __main__
if __name__ == '__main__':
    # Create App object
    app = QApplication(sys.argv)
    
    # Create Widget
    ex = MyWidget()
    

    # If, Widget is closed, Exit Program
    print(app.exec())
    sys.exit(app.exec_())