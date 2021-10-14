import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QWidget, QAction
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title= 'Menu'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUi()

    def initUi(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        helpMenu = mainMenu.addMenu('Help')

        exitButton = QAction( QIcon('exit24.png'), 'Exit', self )
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)

        firstButton = QAction( QIcon('exit24.png'), 'First', self )
        firstButton.setShortcut('Ctrl+A')
        firstButton.setStatusTip('First application')
        firstButton.triggered.connect(self.close)

        enterButton = QAction(QIcon(''), 'Enter', self)
        enterButton.setStatusTip('Enter application')
        enterButton.triggered.connect(self.close)

        fileMenu.addAction(exitButton)
        fileMenu.addAction(firstButton)
        editMenu.addAction(enterButton)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())