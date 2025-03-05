# tb_qt_paint.py

import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PySide6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("tb_qt_paint")
        self.resize(300,100)
        self.show()

    def paintEvent(self, ev):        
        qp = QPainter()
        w, h = self.width(), self.height()
        qp.begin(self)
        
        qp.setBrush(Qt.black)
        qp.setPen(Qt.black)
        qp.drawRect(0, 0, w, h)

        qp.setFont(QFont("Decorative", 10))
        qp.setPen(Qt.white)
        qp.drawText(0, 15, "Ein Demo")

        qp.drawText(ev.rect(), Qt.AlignCenter, "Mitte")
        
        qp.setBrush(Qt.transparent)
        qp.setPen(Qt.yellow)
        qp.drawRect(20, 20, w-40, h-40)
        
        qp.end()

    def keyPressEvent(self, ev):
        key = ev.key() # Keycode ermitteln
    
        if key == Qt.Key_Q: self.close() # Fenster zu
        if key == Qt.Key_R: self.update() # Fenster neu zeichnen     
        ev.accept()

app = QApplication(sys.argv)
w=MyWidget()
sys.exit(app.exec())


              
