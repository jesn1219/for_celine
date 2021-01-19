import sys
from PyQt5.QtWidgets import *
from googletrans import Translator

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        # 위젯 생성
        self.input_label_1 = QLabel('Sentence:', self)
        self.input_edit_1 = QLineEdit(self)
        
        self.result_label_1 = QLabel('Translate Result:', self) 
        self.result_edit_1 = QTextEdit(self)
        self.result_edit_2 = QTextEdit(self)
        self.result_edit_3 = QTextEdit(self)
        
        
        self.translate_button = QPushButton('Translate', self)

        # Translator
        self.translator = Translator()

        # 위젯들을 레이아웃에 배치
        vertical_box_layout = QVBoxLayout() #Vertical Box 레이아웃 사용

        # 차례대로 추가됨.. Vertical 방향으로!
        vertical_box_layout.addWidget(self.input_label_1)
        vertical_box_layout.addWidget(self.input_edit_1)
        vertical_box_layout.addWidget(self.result_label_1)

        vertical_box_layout.addWidget(self.result_edit_1)
        vertical_box_layout.addWidget(self.result_edit_2)
        vertical_box_layout.addWidget(self.result_edit_3)
        
        
        vertical_box_layout.addWidget(self.translate_button)

        # self(가장 큰 위젯)의 레이아웃을, 위에서 설정한 vertical_box_layout으로 설정
        self.setLayout(vertical_box_layout)

        # 버튼에 기능 추가. calcul_btn을 누르면, self.get_result 함수가 실행됨
        self.translate_button.clicked.connect(self.get_translate)


        self.setWindowTitle('Serin\'s Translator')
        self.move(200, 200)
        self.resize(300,200)
        # Same as :
        #self.setGeometry(0, 0, 600, 600)
    
        # Show widget in screen
        self.show()
        
    def get_translate(self):
        text_kor = self.input_edit_1.text()
        text_to_en = self.translator.translate(text_kor, dest='en').text
        text_to_german = self.translator.translate(text_kor, dest='de').text
        text_to_french = self.translator.translate(text_kor, dest='fr').text
        
        self.result_edit_1.setText(text_to_en)
        self.result_edit_2.setText(text_to_german)
        self.result_edit_3.setText(text_to_french)
        
        

  

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