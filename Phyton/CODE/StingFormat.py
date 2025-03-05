#Aufgabe 5:
a = 12
b = 4
# Using str.format()
print("a/dez={}, b/dez={}, a/hex=0x{:x}".format(a, b, a))
# Using an f-string
print(f"a/dez={a}, b/dez={b}, a/hex={hex(a)}")