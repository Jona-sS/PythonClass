from PySide6.QtWidgets import QLabel, QLineEdit, QWidget, QApplication, QPushButton, QGridLayout
import sys
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("HexCalculator")
        grid = QGridLayout()
        grid.addWidget(QLabel("Dezimalzahl"), 0, 0)
        self.dezimal_input = QLineEdit()
        grid.addWidget(self.dezimal_input, 0, 2)
        grid.addWidget(QLabel("Hexzahl"), 1, 0)
        self.hex_output = QLineEdit()        
        grid.addWidget(self.hex_output, 1, 2)
        berechnen_button = QPushButton("Berechnen", self)
        berechnen_button.clicked.connect(self.berechnen)  
        grid.addWidget(berechnen_button, 2, 0, 1, 3)  
        self.setLayout(grid)
        self.show()
    def berechnen(self):
        dezimalzahl = int(self.dezimal_input.text())
        hexzahl = hex(dezimalzahl)
        self.hex_output.setText(hexzahl)

app = QApplication(sys.argv)
w=MyWidget()
app.exec() 