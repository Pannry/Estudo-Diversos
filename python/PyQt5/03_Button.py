import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Button window'
        self.left = 300
        self.top = 300
        self.width = 300
        self.height = 200
        self.initUi()

    def initUi(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        button = QPushButton('PyQt5 Push Button', self)
        button.setToolTip("This is a exemple button!")
        button.move(75, 70)
        button.clicked.connect(self.pressed)

        self.show()

    @pyqtSlot()
    def pressed(self):
        print('PyQt button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
