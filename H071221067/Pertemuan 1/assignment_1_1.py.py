import math

h = float (input('Masukkan nilai h = '))
sudut_a = float (input('Masukkan nilai a = '))
sudut_b = float (input('Masukkan nilai b = '))
# Dengan catatan (90>a>b)

rad_a = (math.pi/180)*sudut_a
rad_b = (math.pi/180)*sudut_b

hasilTan_a = math.tan(rad_a)
hasilTan_b = math.tan(rad_b)

# Misalkan x = panjang kapal
x = h*(hasilTan_a - hasilTan_b)

print(round(x, 1), 'm')