
# temperature.py

"""
Modul zum Umwandeln von Temperaturen zwischen Celsius, Kelvin und
Fahrenheit

"""

def celsius2kelvin(val):
    "Rechne Celsius-Angaben in Kelvin-Angaben um"
    return val + 273

def kelvin2celsius(val):
    "Rechne Kelvin-Angaben in Celsius-Angaben um"
    return val - 273

def celsius2fahrenheit(val):
    "Rechne Celsius-Angaben in Fahrenheit-Angaben um"
    return (val * 9/5) + 32

def fahrenheit2celsius(val):
    "Rechne Fahrenheit-Angaben in Celsius-Angaben um"
    return (val - 32) * 5/9


#print("Diese Zeile wird immer ausgeführt.")
    
if __name__ == "__main__":
    theta = 11
    T=celsius2kelvin(theta)
    theta_p = kelvin2celsius(T)
    print(theta, T, theta_p)
    if theta != theta_p: print("=> Differenz gefunden")

    
