import math
#NOMOR 3 "volume dan luas kerucut"

print("Diketahui :")
r = float(input("Masukkan Jari-jari Kerucut :"))
t = float(input("Masukkan Tinggi Kerucut :"))
PI=math.pi

s =math.sqrt(r**2+t**2)
print(s)
volume = (PI*r**2*t)/3
ls = (PI*r*s)
la = (PI*r**2)
lp = (ls+la)
print ("volume :" , round(volume,2))
print ("Luas Permukaan :" , round(lp,2))