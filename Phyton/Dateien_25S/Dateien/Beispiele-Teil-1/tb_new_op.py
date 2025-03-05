
# tb_new_op.py
from math import sqrt

class MyComplex:
    def __init__(self, rval, ival):
        self.rval = rval
        self.ival = ival

    def __add__(self, obj):
        rval = self.rval
        ival = self.ival
        if isinstance(obj, MyComplex):
            rval += obj.rval
            ival += obj.ival
        else:
            rval += obj
        return MyComplex(rval, ival)


    def __iadd__(self, obj):
        if isinstance(obj, MyComplex):
            self.rval += obj.val
            self.ival += obj.ival
        else:
            self.rval += obj

        return self

    def __abs__(self):
        x, y = self.rval, self.ival
        rv = sqrt(x*x+y*y)
        return rv

    def __str__(self):
        return "MyComplex(%g, %g)" % (self.rval, self.ival)

num1 = MyComplex(2, 3)
num2 = MyComplex(4, 1)
num3 = num1 + num2
num2 += 4

print("num1=", num1)
print("num2=", num2)
print("num3=", num3)
print("abs(num3)=", abs(num3))

