import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super(App, self).__init__()
        self.title = 'PyQt5 layout'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createHorizontalLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("What is your favorite color")
        layout = QHBoxLayout()

        blueButton = QPushButton('Blue', self)
        blueButton.pressed.connect(self.on_click)
        layout.addWidget(blueButton)

        redButton = QPushButton('Red', self)
        redButton.pressed.connect(self.on_click)
        layout.addWidget(redButton)

        greenButton = QPushButton('Red', self)
        greenButton.pressed.connect(self.on_click)
        layout.addWidget(greenButton)

        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def on_click(self):
        print('Button Pressed!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())