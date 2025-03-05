"""
Dieses Modul enthält Funktionen zur Umrechnung zwischen Meter und Zoll.

Funktionen:
- meter2inch(meter): Konvertiert eine Länge von Metern in Zoll.
- inch2meter(inch): Konvertiert eine Länge von Zoll in Meter.
"""

def meter2inch(meter):
    """
    Konvertiert eine Länge von Metern in Zoll.

    Parameter:
    meter (float): Die Länge in Metern.

    Rückgabe:
    float: Die Länge in Zoll.
    """
    return meter * 39.3701

def inch2meter(inch):
    """
    Konvertiert eine Länge von Zoll in Meter.

    Parameter:
    inch (float): Die Länge in Zoll.

    Rückgabe:
    float: Die Länge in Metern.
    """
    return inch / 39.3701