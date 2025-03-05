# tb_qt_slot.py

import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("tb_qt_slot")
        b=QPushButton("Drück mich", self)
        b.clicked.connect(self.onPress)
        b.clicked.connect(self.onAnotherPress)
        self.show()

    def onPress(self):
        print("Button gedrückt 1. Slot")

    def onAnotherPress(self):
        print("Button gedrückt 2. Slot")

app = QApplication(sys.argv)
w=MyWidget()
sys.exit(app.exec())


              
