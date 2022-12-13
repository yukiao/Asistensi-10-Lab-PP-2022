



try:
    mat1_indx11=float(input('input nilai matriks pertama, index 1.1: '))
    mat1_indx12=float(input('input nilai matriks pertama, index 1,2: '))
    mat1_indx21=float(input('input nilai matriks pertama, index 2,1: '))
    mat1_indx22=float(input('input nilai matriks pertama, index 2,2: '))

    mat2_indx11=float(input('input nilai matriks kedua, index 1,1: '))
    mat2_indx12=float(input('input nilai matriks kedua, index 1,2: '))
    mat2_indx21=float(input('input nilai matriks kedua, index 2,1: '))
    mat2_indx22=float(input('input nilai matriks kedua, index 2,2: '))


    matriks1=[[mat1_indx11, mat1_indx12], [mat1_indx21, mat1_indx22]]
    matriks2=[[mat2_indx11, mat1_indx12], [mat2_indx21, mat2_indx22]]

    hasil=[]

    for x in range(0,len(matriks1)):
        row=[]
        for y in range (0,len(matriks1)):
            total = 0
            for z in range(0,len(matriks1)):
                total = total +(matriks1[x][z] * matriks2[z][y])
                row.append(total)
            hasil.append(row)

    print('hasil perkalian matriks')
    print(f'|{matriks1[0][0]}, {matriks2[0][1]}| x |{matriks2[0][0]},{matriks2[0][1]}|')
    print(f'|{matriks1[1][0]}, {matriks2[0][1]}|   |{matriks2[0][0]},{matriks2[0][1]}|')
except:
    print('inputan tidak benar')
    
