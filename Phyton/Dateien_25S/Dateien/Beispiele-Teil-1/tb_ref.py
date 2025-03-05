# tb_ref.py

a=[1,2,3]
b=a
c=list(a)

print("id(a)=%08X" % id(a))
print("id(b)=%08X" % id(b))
print("id(c)=%08X" % id(c))
print("a is b ->", a is b)
print("a is c ->", a is c)
print("a is not c ->", a is not c)


