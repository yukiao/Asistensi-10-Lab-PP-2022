x1 , y1 = map(float, input().split(',')) 
x2 , y2 = map(float, input().split(','))
# Fungsi .split(',') digunakan untuk melakukan inputan dalam baris yang sama, dan dipisahkan dengan koma(,)

jarak = 15

# Rumus yang digunakan untuk mencari panjang radius 
a = (x1 - x2)**2 + (y1 - y2)**2
ar = a**0.5

# Melakukan perkondisian apakah ar lebih kecil sama dengan dari jarak jangkauan(15) atau lebih dari jarak jangkauan(15)
if ar <= jarak:
    print('dalam jangkauan') # Jika lebih kecil sama dengan
else:
    print('tidak dalam jangkauan') # Jika hasilnya lebih dari