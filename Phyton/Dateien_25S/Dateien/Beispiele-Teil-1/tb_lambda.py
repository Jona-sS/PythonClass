# tb_lambda.py

def foreach(f, *args):
    res=[]
    for arg in args: res.append(f(arg))
    return res

vec=foreach(lambda x: 2*x*x, 1, 2, 3)
print(vec)

# Ausgabe:
# [2, 8, 18]


print(type(lambda x: 2*x*x))
# Ausgabe: <class 'function'>
