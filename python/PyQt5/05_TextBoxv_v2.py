from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit,
                             QMessageBox, QLabel, QSpinBox, QMainWindow)
from PyQt5.QtCore import pyqtSlot
import sys


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.title = 'Soma'
        self.left = 300
        self.top = 300
        self.width = 400
        self.height = 80
        self.initUi()

    def initUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        option = QMessageBox.question(self, "Formas diferentes de somar.",
                                      "[No ] para QSpinBox, \n[Yes] para QLineEdit", QMessageBox.Yes| QMessageBox.No,
                                      QMessageBox.Yes)


        if option == QMessageBox.Yes:
            self.sum = AppSum1()
        else:
            self.sum = AppSum2()

        self.setCentralWidget(self.sum)
        self.show()



class AppSum(QWidget):
    def __init__(self):
        super(AppSum, self).__init__()
        # create textbox
        self.text1 = 0

        # label '+'
        self.sum = QLabel("+", self)
        self.sum.move(130, 30)

        # create textbox
        self.text2 = 0

        # create a push button in window
        self.button = QPushButton("Hit me to sum", self)
        self.button.move(280, 25)

        # connect the button with function on_click
        self.button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        textValue = 0
        QMessageBox.question(self, "Titulo da Caixa Soma", "Soma: " + str(textValue), QMessageBox.Ok, QMessageBox.Ok)


class AppSum1(AppSum):
    def __init__(self):
        super(AppSum1, self).__init__()
        # create textbox
        self.text1 = QLineEdit(self)
        self.text1.move(20, 20)
        self.text1.resize(100, 40)
        self.text1.setText("15")

        # create textbox
        self.text2 = QLineEdit(self)
        self.text2.move(150, 20)
        self.text2.resize(100, 40)
        self.text2.setText("20")

    @pyqtSlot()
    def on_click(self):
        textValue = int(self.text1.text()) + int(self.text2.text())
        QMessageBox.question(self, "Titulo da Caixa Soma", "Soma: " + str(textValue), QMessageBox.Ok, QMessageBox.Ok)


class AppSum2(AppSum):
    def __init__(self):
        super(AppSum2, self).__init__()
        # create textbox
        self.text1 = QSpinBox(self)
        self.text1.setRange(0, 10000)
        self.text1.move(20, 20)
        self.text1.resize(100, 40)
        self.text1.setValue(15)

        # create textbox
        self.text2 = QSpinBox(self)
        self.text2.setRange(0, 10000)
        self.text2.move(150, 20)
        self.text2.resize(100, 40)
        self.text2.setValue(20)

    @pyqtSlot()
    def on_click(self):
        textValue = self.text1.value() + self.text2.value()
        QMessageBox.question(self, "Titulo da Caixa Soma", "Soma: " + str(textValue), QMessageBox.Ok, QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
