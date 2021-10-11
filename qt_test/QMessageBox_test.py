import sys

from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        
    def closeEvent(self,event):
        reply = QMessageBox.question(self, 'Message',
            'Are you Ok?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
