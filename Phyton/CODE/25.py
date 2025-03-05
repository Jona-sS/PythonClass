class Shape:
    __id_counter=0
    def __init__(self):
        Shape.__id_counter += 1
        self.__id = Shape.__id_counter
    def get_id(self):
        return self.__id
    def draw(painter):pass
    def moveBy(dx, dy):pass

class Rect(Shape):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.x=0
        self.y=0
        self.w=0
        self.h=0
    def moveBy(self,dx, dy):
        self.x+=dx
        self.y+=dy
class Line(Shape):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.x=0
        self.y=0
        self.w=0
        self.h=0
    def moveBy(dx, dy):
        self.x+=dx
        self.y+=dy

#Test Code
s1 = Rect(0, 0, 10, 50) 
s2 = Line(0, 0, 50, 10) 
painter = None 
s1.draw(painter) 
s2.draw(painter) 
s2.moveBy(5, 10) 
s2.draw(painter) 