
# tb_read.py

f=open("tabelle.txt", "r")
for line in f:
    li=line.strip()
    print(li, end=" => ")
    dat=li.split()
    print(dat)
    
f.close()
