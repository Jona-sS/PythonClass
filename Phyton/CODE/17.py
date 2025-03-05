d=dict(a=3, b=5, c="hallo")
def write_xml(filename, dictionary):
    f=open(filename, mode="w")
    f.write("<?xml version='1.0' encoding='UTF-8'?>\n<dict>\n")
    for key in dictionary:
        f.write(f"<entry>\n\t<key>{key}</key>\n\t<value>{dictionary[key]}</value>\n</entry>\n") 
    f.write("</dict>")
    f.close()

write_xml("test.xml", d)
#Zusatz: auslesen der Datei
idx = 0
endidx =0
pos = 0
f=open("test.xml", "r")
for line in f:
    li=line.strip()
    idx = li.find(">", pos)
    endidx = li.find("<", pos)
    pos=endidx+1 #zum neuen Suchen muss die Postion hinter der > gesetzt werden,
    #da sonst immer wieder das gleiche Ergebnis gefunden wird
    print(li[idx:endidx+1])
    #print(li, end=" => ")
    dat=li.split()
    print(dat)
f.close()