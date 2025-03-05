idx = 0 
val = 2 
seq = [1, 2] 
try:
    neuwert = seq[idx] 
    schwelle = 42 / val 
    print("Schwelle =", schwelle) 
except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt.")
except IndexError:
    print("Fehler: Index außerhalb des gültigen Bereichs.")
except Exception as e:
    print("Unbekannter Fehler:", str(e))