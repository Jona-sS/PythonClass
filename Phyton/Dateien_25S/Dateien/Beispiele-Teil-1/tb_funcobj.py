
# tb_funcobj.py

def foreach(f, *args):
    res=[]
    for arg in args:
        res.append(f(arg))
    return res

def square(x): return x*x
vec=foreach(square, 1, 2, 3)
print(vec)
