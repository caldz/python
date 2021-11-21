import sys
from PyQt5.QtWidgets import QWidget, QApplication
from WcwConstruct import WcwConstruct

class WorkCalWin(QWidget):
    def __init__(self):
        super().__init__()
        wc = WcwConstruct()
        wc.setup(self)
        self.show()

if __name__ == '__main__':
    print('hi')
    app = QApplication(sys.argv)
    wcw = WorkCalWin()
    sys.exit(app.exec_())
