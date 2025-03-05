
# tb_write.py

f=open("tabelle.txt", "w")

for idx in range(32, 128):
    f.write("%3d %c\n" % (idx, chr(idx)))    
f.close()
