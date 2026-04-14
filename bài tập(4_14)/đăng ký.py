from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys

class Test(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("register.ui", self)   # load trực tiếp file .ui

app = QApplication(sys.argv)
w = Test()
w.show()
sys.exit(app.exec())