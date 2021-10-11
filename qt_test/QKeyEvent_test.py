import sys
from PyQt5.QtWidgets import QWidget,QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
    def keyReleaseEvent(self,e):
        print('key='+e.text())
        if e.text()=='q':
            self.close()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    e=Example()
    sys.exit(app.exec_())
