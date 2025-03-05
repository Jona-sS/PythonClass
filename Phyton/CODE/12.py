
d={1000:"Kartoffeln", 1020:"Gurken", 720:"Bananen", 702:"Kiwis",
5000:"Schokolade", 5010:"Kartoffelchips"} 
idx=int(input("Geben Sie die Nummer ein: "))
print(d.get(idx, "Produkt nicht gefunden"))