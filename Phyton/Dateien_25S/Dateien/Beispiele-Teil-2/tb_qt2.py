# tb_qt2.py

import sys

from PySide6.QtWidgets import QApplication, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 200)
        self.setWindowTitle("tb_qt2")
        self.show()

app = QApplication(sys.argv)
w=MyWidget()
app.exec()
