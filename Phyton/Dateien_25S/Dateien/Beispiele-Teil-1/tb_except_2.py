# tb_except_2.py

def make_frac(txt):
    if txt.lower() == "inf":
        raise NotImplementedError("inf")
    if txt.lower() == "nan":
        raise NotImplementedError("nan")
    inval=float(txt)
    return 1/inval

try:
    txt=input("Nenner für 1/Zahl eingeben:")
    num=make_frac(txt)
except ZeroDivisionError:
    print("1/0 geht nicht")
except ValueError:
    print("Sie haben keine Zahl eingegeben")
except Exception as e:
    # Fehlerobjekt kann auch an eine Variable zugewiesen werden
    print("Fehler:", e.__class__, e.args)
else:
    # wird ausgeführt, wenn angegeben und kein Fehler im try-Block
    print("Bruch 1/%s=%f" % (txt, num))
finally:
    # wird am Schluss immer ausgeführt, wenn angegeben
    print("Ende der Berechnung")


    
