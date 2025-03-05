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

#Test Code
s1 = Rect(0, 0, 10, 50) 
s2 = Line(0, 0, 50, 10) 
s3 = Group() 
s3.addShape(s1) 
s3 += s2 
painter = None 
s2.draw(painter) 
s3.moveBy(5, 10) 
s3.draw(painter) 