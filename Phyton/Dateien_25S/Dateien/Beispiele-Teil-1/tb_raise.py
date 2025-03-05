# tb_raise.py

def make_frac(txt):
    if txt.lower() == "inf":
        raise NotImplementedError("inf")
    if txt.lower() == "nan":
        raise NotImplementedError("nan")
    inval=float(txt)
    return 1/inval


txt=input("Nenner für 1/Zahl eingeben:")
num=make_frac(txt)
print("Bruch 1/%s=%g" % (txt, num))
print("Ende der Berechnung")
