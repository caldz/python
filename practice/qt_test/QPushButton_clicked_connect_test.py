import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        btn=QPushButton('hehe',self)
        btn.clicked.connect(self.close)
        self.show()        
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
