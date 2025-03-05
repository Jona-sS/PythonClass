g_dict = {}
g_list = []
class WinRect:
    def __init__(self, x, y, w, h, descr=""):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.descr = descr  

f=open("rects.txt", "r")
for line in f:
    parts=line.strip().split(':')
    if len(parts)!=5: continue
    obj=WinRect(int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]), parts[4])
    g_dict[parts[4]]=obj
    g_list.append(obj)
f.close()

descr=input("Enter a keyword: ")
obj=g_dict.get(descr)
if obj:
    print(f"found: {obj.x},{obj.y},{obj.w},{obj.h}")
else:
    print("not found")