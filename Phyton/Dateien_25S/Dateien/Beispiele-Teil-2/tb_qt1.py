# tb_qt1.py

import sys

from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
w=QWidget()
w.resize(300, 200)
w.setWindowTitle("tb_qt1")
w.show()
app.exec()
