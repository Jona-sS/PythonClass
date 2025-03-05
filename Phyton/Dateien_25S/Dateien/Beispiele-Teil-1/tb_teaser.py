
# tb_teaser.py

# Python-Programm

def conv(zahl):
    text = ''

    while zahl > 0:
        ziffer = zahl % 2
        zahl //= 2
        if ziffer == 1:
            zeichen = '1'
        else:
            zeichen = '0'

        text = zeichen + text
        
    return text


zahl = int(input("Zahl eingeben: "))
print(conv(zahl))
