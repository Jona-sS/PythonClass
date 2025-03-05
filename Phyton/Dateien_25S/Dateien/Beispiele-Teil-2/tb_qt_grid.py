# tb_qt_grid.py

import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtWidgets import QGridLayout


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("tb_qt_grid")
        grid = QGridLayout()
        grid.addWidget(QPushButton("A", self), 0, 0)
        grid.addWidget(QPushButton("B", self), 0, 1)
        grid.addWidget(QPushButton("C", self), 0, 2)
        grid.addWidget(QPushButton("D", self), 1, 0, 1, 2)        
        grid.addWidget(QPushButton("E", self), 1, 2)
        grid.addWidget(QPushButton("F", self), 2, 0, 1, 3)        
            
        self.setLayout(grid)
        self.show()


app = QApplication(sys.argv)
w=MyWidget()
sys.exit(app.exec())


              
