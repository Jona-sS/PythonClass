# tb_error.py

def make_frac(txt):
    inval=float(txt)
    return 1/inval

txt=input("Nenner für 1/Zahl eingeben:")
num=make_frac(txt)
print("Bruch 1/%s=%f" % (txt, num))
print("Ende der Berechnung")


    
