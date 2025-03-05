# tb_except_3.py

def func():
    try:
        return "one"
    finally:
        return "two"


# Ausgabe ist immer two
print(func())

# Minimaler try-except-Aufruf
try:
    raise Exception("test it again")
except:
    print("** exception occured **")

# Minimaler try-finally-Aufruf
try:
    raise Exception("test it")
finally:
    print("** we will always be called **")
