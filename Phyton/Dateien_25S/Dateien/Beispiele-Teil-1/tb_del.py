# tb_del.py

class C:
    def __init__(self, name=""):
        self.name = name
        print("init of %s: id=%08X" \
              % (self.name, id(self)))

    def __del__(self):
        print("fini of %s, id=%08X" \
              % (self.name, id(self)))

clist=[C("c%d" % idx) for idx in range(5)]
print("** remove items")
clist[2]=None
del clist[3]
print("** clist")
for c in clist: print(c)
print("** end of prog")
