
# tb_num_tree.py

from math import sqrt

def roman2float(txt): return 42 # Berechnung hier unwichtig

class Number:
    def __init__(self, val): self.val = val
    def getAbs(self):
        rv = self.val
        return rv if rv >= 0 else -rv

class Roman(Number):
    def __init__(self, val):
        self.val = roman2float(val)
        self.txt = val
    
class Complex(Number):
    def __init__(self, rval, ival):
        self.val = rval
        self.ival = ival

    def getAbs(self):
        x, y = self.val, self.ival
        rv = sqrt(x*x+y*y)
        return rv
    

a=Number(3.4)
b=Roman("IX")
c=Complex(1, -2)

nums=(a,b,c)
for num in nums: print(num.getAbs())

        
