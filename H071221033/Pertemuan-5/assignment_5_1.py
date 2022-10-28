# perkalian matriks menggunakan list
list11 = []
for baris1 in range(1,3):
    list21 = []
    for kolom1 in range(1,3):
        matriks1 = int(input(f'Input nilai matriks pertama index {baris1},{kolom1}:'))
        list21.append(matriks1)
    list11.append(list21)

list21 = []
for baris2 in range(1,3):
    list22 = []
    for kolom2 in range(1,3):
        matriks2 = int(input(f'Input nilai matriks kedua index {baris2},{kolom2}:'))
        list22.append(matriks2)
    list21.append(list22)

hasilkali1 = []
hasilkali2 = []

b1k1 = (list11[0][0]*list21[0][0])+(list11[0][1]*list21[1][0])
hasilkali1.append(b1k1)
b1k2 = (list11[0][0]*list21[0][1])+(list11[0][1]*list21[1][1])
hasilkali1.append(b1k2)
b2k1 = (list11[1][0]*list21[0][0])+(list11[1][1]*list21[1][0])
hasilkali2.append(b2k1)
b2k2 = (list11[1][0]*list21[0][1])+(list11[1][1]*list21[1][1])
hasilkali2.append(b2k2)

print('Hasil perkalian matriks')
print(f'| {list11[0][0]}, {list11[0][1]} | x | {list21[0][0]}, {list21[0][1]} | = | {hasilkali1[0]}, {hasilkali1[1]} |')
print(f'| {list11[1][0]}, {list11[1][1]} |   | {list21[1][0]}, {list21[1][1]} |   | {hasilkali2[0]}, {hasilkali2[1]} |')