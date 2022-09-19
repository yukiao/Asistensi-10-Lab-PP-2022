import math

print("Program Menghitung Volume dan Luas Permukaan Kerucut")

jari=float(input("Masukkan Jari Jari Alas : "))
tinggi=float(input("Masukkan Tinggi : "))

pelukis=math.sqrt((jari**2)+(tinggi**2))

luas_permukaan=float(math.pi*jari*(jari+pelukis))
volume=float((1/3)*math.pi*(jari**2)*tinggi)

print("volume Kerucut = ", round(volume,2))
print("luas permukaan = ", round(luas_permukaan,2))
