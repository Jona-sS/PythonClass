import temperature
#Main aus temperature.py
theta = 11
T=temperature.celsius2kelvin(theta)
theta_p = temperature.kelvin2celsius(T)
print(theta, T, theta_p)
if theta != theta_p: print("=> Differenz gefunden")


#ergänze Umrechnung
print(temperature.celsius2fahrenheit(30))