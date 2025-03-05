# tb_qt_close.py

import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox as QMB

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("tb_qt_close")
        self.resize(300,100)
        self.show()

    def closeEvent(self, ev):
        r = QMB.question(self, "Abfrage", "Wirklich Beenden?",
                         QMB.Yes | QMB.No, QMB.No)
        if r == QMB.Yes:
            ev.accept()
        else:
            ev.ignore()


    def hideEvent(self, ev):
        print("Fenster verschwindet", ev, self)

    def showEvent(self, ev):
        print("Fenster zeigt sich", ev, self)

app = QApplication(sys.argv)
w=MyWidget()
sys.exit(app.exec())


              
