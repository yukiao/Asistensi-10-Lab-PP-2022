import math
#Nur amalia
#H071221016
#Menghitung Panjang Kapal

print ('---Menghitung Panjang Kapal---')
print ('------------------------------')

print ('Diketahui :')
h = int(input('Tinggi Menara (m)                  : '))
a = int(input('Sudut Elevasi Ujung Depan Kapal    : '))
b = int(input('Sudut Elevasi Ujung Belakang Kapal : '))

x = math.tan(b*0.0174533)*h
y = math.tan(a*0.0174533)*h

panjang_kapal = y-x

print ('panjang kapal : ',round(panjang_kapal,1),'m')
