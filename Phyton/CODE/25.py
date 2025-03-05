class Shape:
    __id_counter=0
    def __init__(self):
        self.__id = Shape.__id_counter
        Shape.__id_counter += 1
    def get_id(self):
        return self.__id
    def draw(self,painter):pass
    def moveBy(self,dx, dy):pass

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
    def draw(self,painter):
        print(f"line: id #{self.get_id()} x={self.x}, y={self.y}, w={self.w}, h={self.h}")

#Test Code
s1 = Rect(0, 0, 10, 50) 
s2 = Line(0, 0, 50, 10) 
painter = None 
s1.draw(painter) 
s2.draw(painter) 
s2.moveBy(5, 10) 
s2.draw(painter) 