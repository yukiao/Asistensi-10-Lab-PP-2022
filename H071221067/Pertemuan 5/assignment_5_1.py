try:
    m1_idx11 = float(input('Input nilai matriks pertama, index 1,1: '))
    m1_idx12 = float(input('Input nilai matriks pertama, index 1,2: '))
    m1_idx21 = float(input('Input nilai matriks pertama, index 2,1: '))
    m1_idx22 = float(input('Input nilai matriks pertama, index 2,2: '))

    m2_idx11 = float(input('Input nilai matriks kedua, index 1,1: '))
    m2_idx12 = float(input('Input nilai matriks kedua, index 1,2: '))
    m2_idx21 = float(input('Input nilai matriks kedua, index 2,1: '))
    m2_idx22 = float(input('Input nilai matriks kedua, index 2,2: '))

    matriks1 = [[m1_idx11, m1_idx12], [m1_idx21, m1_idx22]]
    matriks2 = [[m2_idx11, m2_idx12], [m2_idx21, m2_idx22]]
    hasil = []

    for x in range(0, len(matriks1)):
        row = []
        for y in range(0, len(matriks1[0])):
            total = 0
            for z in range(0, len(matriks1)):
                total = total + (matriks1[x][z] * matriks2[z][y])
            row.append(total)
        hasil.append(row)

    print('Hasil perkalian matriks')
    print(f"|{matriks1[0][0]}, {matriks1[0][1]}| x |{matriks2[0][0]}, {matriks2[0][1]}| = |{hasil[0][0]}, {hasil[0][1]}|")
    print(f"|{matriks1[1][0]}, {matriks1[1][1]}|   |{matriks2[1][0]}, {matriks2[1][1]}|   |{hasil[1][0]}, {hasil[1][1]}|")
except:
    print('Inputan tidak benar')