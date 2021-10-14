import sys
from PyQt5.QtWidgets import QApplication, QWidget

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('First UI')
        self.setGeometry(100, 100, 200, 200)
        self.show()


if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())