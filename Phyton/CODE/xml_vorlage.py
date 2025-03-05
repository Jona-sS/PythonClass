xmltxt="""<?xml version="1.0" encoding="UTF-8"?>
<quiz>
 <question>
  <text>Kann ein String in Python verändert werden?</text>
  <solution>Nein, für Änderungen muss er neu zusammengesetzt werden.</solution>
 </question>
</quiz>
"""
pos = 0
endidx =0
while True:
    idx = xmltxt.find("<", pos)
    endidx = xmltxt.find(">", pos)
    pos=endidx+1 #zum neuen Suchen muss die Postion hinter der > gesetzt werden,
    #da sonst immer wieder das gleiche Ergebnis gefunden wird
    print(xmltxt[idx:endidx+1])
    if idx < 0: break

    # hier kommen Ihre Ergänzungen