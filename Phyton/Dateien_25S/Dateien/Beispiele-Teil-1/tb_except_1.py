# tb_except_1.py

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
    print("Bruch 1/%s=%g" % (txt, num))
except Exception:
    print("Fehler")
