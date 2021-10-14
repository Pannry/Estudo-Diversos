from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QLabel, QSpinBox
from PyQt5.QtCore import pyqtSlot
import sys

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Text Box'
        self.left = 300
        self.top = 300
        self.width = 400
        self.height = 80
        self.initUi1()

    def initUi1(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #create textbox
        self.text1 = QLineEdit(self)
        self.text1.move(20, 20)
        self.text1.resize(100, 40)
        self.text1.setText("15")

        # label '+'
        self.sum = QLabel("+", self)
        self.sum.move(130, 30)

        #create textbox
        self.text2 = QLineEdit(self)
        self.text2.move(150, 20)
        self.text2.resize(100, 40)
        self.text2.setText("20")

        # create a push button in window
        self.button = QPushButton("Hit me to sum", self)
        self.button.move(280, 25)

        #connect the button with function on_click
        self.button.clicked.connect(self.on_click1)

        self.show()

    def initUi2(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #create textbox
        self.text1 = QSpinBox(self)
        self.text1.setRange(0, 10000)
        self.text1.move(20, 20)
        self.text1.resize(100, 40)
        self.text1.setValue(15)

        # label '+'
        self.sum = QLabel("+", self)
        self.sum.move(130, 30)

        #create textbox
        self.text2 = QSpinBox(self)
        self.text2.setRange(0, 10000)
        self.text2.move(150, 20)
        self.text2.resize(100, 40)
        self.text2.setValue(20)


        # create a push button in window
        self.button = QPushButton("Hit me to sum", self)
        self.button.move(280, 25)

        #connect the button with function on_click
        self.button.clicked.connect(self.on_click2)

        self.show()

    @pyqtSlot()
    def on_click1(self):
        textValue = int(self.text1.text()) + int(self.text2.text())
        QMessageBox.question(self, "Titulo da Caixa Soma", "Soma: "+str(textValue), QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def on_click2(self):
        textValue = self.text1.value() + self.text2.value()
        QMessageBox.question(self, "Titulo da Caixa Soma", "Soma: " + str(textValue), QMessageBox.Ok, QMessageBox.Ok)


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())