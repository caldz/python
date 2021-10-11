import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        btn=QPushButton('button',self)
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    e=Example()
    sys.exit(app.exec_())
