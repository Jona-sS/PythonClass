def get_ones(val):
    binary = bin(val)
    return binary.count('1')
def sort_by_ones(seq:list): 
    #:list ist optional, stellt sicher das .copy() funktioniert
    seqk=seq.copy()
    seqk.sort(key=get_ones) 
    #nicht direkt in die return Zeile, da None als Rückgabe (This wird geändert)
    return seqk

def  get_bits_as_list(val):
    bString = "{:b}".format(val) #alternativ als f-string: f"{val:b}"
    return list(bString)
#Test:
l= [1,0x21,7,0x80,0,0b1111]
print(l)
print(sort_by_ones(l))
print(get_bits_as_list(26))