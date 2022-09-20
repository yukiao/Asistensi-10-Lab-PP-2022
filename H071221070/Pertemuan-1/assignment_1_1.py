h = int(input('Masukkan tinggi menara: '))
a = int(input('Masukkan sudut elevasi pengamat terhadap ujung depan kapal: '))
b = int(input('Masukkan sudut elevasi pengamat terhadap ujung belakang kapal: '))

import math 
x = math.tan(a*(math.pi/180))*h
y = math.tan(b*(math.pi/180))*h

panjang_kapal = (x - y)
print ('panjang dari kapal adalah: ' , round(panjang_kapal, 1) , 'm')