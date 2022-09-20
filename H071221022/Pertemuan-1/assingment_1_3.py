from math import pi
t = float(input("masukan tinggi : "))
r = float( input( " masukkan jari-jari : "))
s = (t**2 + r**2)**(1/2)
V = (1/3)*(pi)*r*r*t
L = (pi)*r*(s + r)

print (F"> volume : {round(V, 2)}")
print (F"> Luas permukaan  : {round(L, 2)}")