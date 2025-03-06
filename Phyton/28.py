import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PySide6.QtCore import Qt
class Shape:
    __id_counter=0
    def __init__(self):
        self.__id = Shape.__id_counter
        Shape.__id_counter += 1
    def get_id(self):
        return self.__id
    def draw(self,painter):pass
    def moveBy(self,dx, dy):pass
class Group(Shape):
    def __init__(self):
        super().__init__()
        self.shapes=[]
    def addShape(self,obj):
        self.shapes.append(obj)
    def __iadd__(self,obj) :
        self.shapes.append(obj)
        return self
    def draw(self,painter):
        print(f"group: id #{self.get_id()} num_shapes={len(self.shapes)}")
        for obj in self.shapes:
            obj.draw(painter)
    def moveBy(self,dx, dy):
        for obj in self.shapes:
            obj.moveBy(dx,dy)
class Rect(Shape):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def moveBy(self,dx, dy):
        self.x+=dx
        self.y+=dy
    def draw(self,painter):
        print(f"rect: id #{self.get_id()} x={self.x}, y={self.y}, w={self.w}, h={self.h}")
        painter.setBrush(Qt.transparent)
        painter.setPen(Qt.red)
        painter.drawRect(self.x, self.y, self.w, self.h)

class Line(Shape):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def moveBy(self,dx, dy):
        self.x+=dx
        self.y+=dy
        self.w+=dx
        self.h+=dy
    def draw(self,painter):
        print(f"line: id #{self.get_id()} x={self.x}, y={self.y}, w={self.w}, h={self.h}")
        painter.setBrush(Qt.transparent)
        painter.setPen(Qt.red)
        painter.drawLine(self.x, self.y, self.w, self.h)
        

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Vektrografik")
        self.resize(200,200)
        self.show()
        self.g=Group() 
        self.g.addShape(Line(20,  50, 20, 100)) 
        self.g.addShape(Line(20, 100, 40, 110)) 
        self.g.addShape(Line(40, 110, 60, 100)) 
        self.g.addShape(Line(60, 100, 60,  50)) 
        self.g.addShape(Line(60,  50, 40,  40)) 
        self.g.addShape(Line(40,  40, 20,  50)) 
        self.g.addShape(Line(25,  85, 40,  95)) 
        self.g.addShape(Line(40,  95, 55,  85)) 
        self.g.addShape(Rect(45, 60, 5 ,5)) 
        self.g.addShape(Rect(30, 60, 5 ,5))

    def paintEvent(self, ev):
        qp = QPainter()
        w, h = self.width(), self.height()
        qp.begin(self)
        
        qp.setBrush(Qt.gray)
        qp.setPen(Qt.gray)
        qp.drawRect(0, 0, w, h)
        self.g.draw(qp)
        qp.end()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.g.moveBy(-5, 0)
        elif event.key() == Qt.Key_Right:
            self.g.moveBy(5, 0)
        elif event.key() == Qt.Key_Up:
            self.g.moveBy(0, -5)
        elif event.key() == Qt.Key_Down:
            self.g.moveBy(0, 5)
        self.update()
app = QApplication(sys.argv)
w=MyWidget()
sys.exit(app.exec())#beendet das Programm, alles folgende wird nicht ausgeführt
