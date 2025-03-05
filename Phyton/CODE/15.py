list = ["0023", "-11", "7"]
listk = list.copy()
listk.sort(key=lambda x: abs(int(x)))
#.sort() hat keine normalen Übergabewerte
print(list)
print(listk)
#Zusatz: List Comprehension:
listPositive = [int(x) for x in list if int(x) > 0]
#Int Werte von list kopieren wenn >0
print(listPositive)