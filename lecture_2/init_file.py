import sys
from PyQt5.QtWidgets import *


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Inital format file')
        
        self.move(0, 0)
        self.resize(600,600)
        # Same as :
        #self.setGeometry(0, 0, 600, 600)
    
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