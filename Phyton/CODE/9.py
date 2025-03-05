a=(1) 
b=([1],[2]) 
c="Sonnenschein" 
#print(a[0]) int kann mann nicht indexieren, a=(1,) wäre ein Tubel und würde gehen
#c[1]="O" im Stings kann mann nicht einzelne Buchstaben ändern
#b[0]=3 Tubel kann man nich ändern
d=b 
b[0][0]=4 
d[1].append(None) 
print(a,b) 
print(len(d)) 