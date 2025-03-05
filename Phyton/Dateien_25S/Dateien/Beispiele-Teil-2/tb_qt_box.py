# tb_qtbox.py

import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("tb_qtbox")
        box = QVBoxLayout()

        box.addWidget(QPushButton("A", self))
        box.addStretch()
        box.addWidget(QPushButton("B", self))
        box.addWidget(QPushButton("C", self))
        box.addStretch()
        box.addWidget(QPushButton("D", self))
            
        self.setLayout(box)
        self.show()


app = QApplication(sys.argv)
w=MyWidget()
sys.exit(app.exec())


              
