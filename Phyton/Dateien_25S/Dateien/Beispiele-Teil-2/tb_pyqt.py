# tb_pyqt.py

import sys

from PyQt6.QtWidgets import QApplication, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 200)
        self.setWindowTitle("tb_pyqt")
        self.show()

app = QApplication(sys.argv)
w=MyWidget()
app.exec_()
