import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QFormLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton,
                             QSpinBox, QWidget)
from PyQt5.QtGui import QStaticText


class App(QMainWindow):
    """docstring for App."""
    def __init__(self):
        super(App, self).__init__()
        self.title = "Basic App"
        self.top = 200
        self.left = 200
        self.width = 200
        self.height = 75
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.sum = AppSum()
        self.setCentralWidget(self.sum)
        self.show()

class AppSum(QWidget):
    """docstring for ."""
    def __init__(self):
        super(AppSum, self).__init__()

        self.layout = QFormLayout()

        # Create horizontal layout and place spinboxes on it
        self.input_layout = QHBoxLayout()
        self.input_value_o = QSpinBox()
        self.input_value_o.setRange(0, 1000000)
        self.input_value_t = QSpinBox()
        self.input_value_t.setRange(0, 1000000)
        self.input_layout.addWidget(self.input_value_o)
        self.input_layout.addWidget(self.input_value_t)

        # Create horizontal layout and place button and label on it
        self.result_layout = QHBoxLayout()
        self.result_text = QLabel("Resultado")
        self.sum_button = QPushButton("Soma")
        self.sum_button.clicked.connect(self.my_sum)
        self.result_layout.addWidget(self.sum_button)
        self.result_layout.addWidget(self.result_text)

        self.layout.addRow(self.input_layout)
        self.layout.addRow(self.result_layout)

        self.setLayout(self.layout)

    def my_sum(self):
        result = self.input_value_o.value() + self.input_value_t.value()
        print("yee")
        self.result_text.setText(str(result))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())