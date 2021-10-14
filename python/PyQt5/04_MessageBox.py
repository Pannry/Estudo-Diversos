import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Message Box'
        self.left = 300
        self.top = 300
        self.width = 300
        self.height = 200
        self.initUi()

    def initUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #               QMessageBox.question(self, messageBox title, message in box,
        #                                    Opçoes que irão aparecer, aonde o cursor ira começar)

        buttonMessage = QMessageBox.question(self, "pyqt5 message", 'Do you like qt5?',
                                             QMessageBox.Yes | QMessageBox.No , QMessageBox.Yes)

        if buttonMessage == QMessageBox.Yes:
            print('Yes Clicked')
        else:
            print('No Clicked')

        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())

