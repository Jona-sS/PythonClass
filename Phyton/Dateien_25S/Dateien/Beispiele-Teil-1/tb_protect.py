# tb_protect.py

class C:
    __cvar = 1
    _avar = 2
    def __init__(self): self.__var = 1
    def get_var(self): return self.__var * self.__cvar

# Fehler in print, wenn if 1:! __cvar wird in C nicht gefunden
if 0: print(C.__cvar)

# Der Trick: __cvar wurde umbenannt in _C__cvar
# Schema: Unterstrich + Klassenname voranstellen
print(C._C__cvar) 

# kein spezieller Schutz => _avar wurde nicht umbenannt
# eine solche Verwendung aber als schlechte Praxis betrachtet
print(C._avar)

c=C()
print(c._C__cvar)   # gleiches Verhalten wie oben
if 0: print(c.__var)      # Fehler in print wg. Umbenennung!
print(c._C__var)    # okay

