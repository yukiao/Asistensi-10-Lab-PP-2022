list11=[]
for baris1 in range(1,3):
    list21=[]
    for kolom1 in range(1,3) :
        matriks1=int(input(f'Input nilai matriks pertama index {baris1},{kolom1}:'))
        list21.append(matriks1)
    list11.append(list21)

list21=[]
for baris2 in range(1,3):
    list22=[]
    for kolom2 in range(1,3) :
        matriks2=int(input(f'Input nilai matriks kedua index {baris2},{kolom2}:'))
        list22.append(matriks2)
    list21.append(list22)

multiplier1=[]
multiplier2=[]

r1c1=(list11[0][0]*list21[0][0])+(list11[0][1]*list21[1][0])
multiplier1.append(r1c1)
r1c2=(list11[0][0]*list21[0][1])+(list11[0][1]*list21[1][1])
multiplier1.append(r1c2)
r2c1=(list11[1][0]*list21[0][0])+(list11[1][1]*list21[1][0])
multiplier2.append(r2c1)
r2c2=(list11[1][0]*list21[0][1])+(list11[1][1]*list21[1][1])
multiplier2.append(r2c2)

print('Hasil perkalian matriks')
print(f'| {list11[0][0]}, {list11[0][1]} | x | {list21[0][0]}, {list21[0][1]} | = | {multiplier1[0]}, {multiplier1[1]} |')
print(f'| {list11[1][0]}, {list11[1][1]} |   | {list21[1][0]}, {list21[1][1]} |   | {multiplier2[0]}, {multiplier2[1]} |')