z=1/0 #ZeroDivisionError: division by zero
print(a)#NameError: name 'a' is not defined
lst=[1,2,3]
print(lst[3])#IndexError: list index out of range
d={'a':1}  
print(d['b'])#KeyError: 'b'
def f(a): return a
f()#TypeError: f() missing 1 required positional argument: 'a'
import x #ModuleNotFoundError: No module named 'x'
x.y #AttributeError: module 'x' has no attribute 'y
int('a')#ValueError: invalid literal for int() with base 10: 'a'