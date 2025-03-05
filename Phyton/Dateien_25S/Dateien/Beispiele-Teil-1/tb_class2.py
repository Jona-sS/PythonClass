# tb_class2.py

# leere Klasse
class K:
    pass

# Klasse instanziieren
c=K()

# nachträglich Element an Instanz anfügen geht auch
# dann aber nicht in Klasse K enthalten
c.var1 = 43

# nachträglich Attribut an Klasse anfügen geht auch
K.kvar = "kvar"

# Instanz bekommt das auch mit
print(c.kvar)


class KA:
    def get_var1(self): return self.kvar

    def change(self, val):
        self.dynval = val

ca=KA()
# wir rufen Methode von KA für Instanz c der Klasse K auf
# Instanz c hat keinerlei Beziehung zu Klasse KA
# Code lässt sich aber ohne Probleme ausführen
print(KA.get_var1(c))

# auch Zuweisung von Werten kein Problem, wenn Instanz nicht zur Klasse
# der verwendeten Methode gehört
# Python macht keinen Typcheck
KA.change(c, 100)
print(c.dynval)


