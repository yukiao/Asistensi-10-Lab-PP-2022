try:
    a, b, c, d, e= [int(x) for x in input("Masukkan Lima Angka = ").split()]
except:
    print("Inputan Tidak Valid")
else:
    jmlGenap=0
    jmlGanjil=0
    jmlPositif=0
    jmlNegatif=0
    angka=[a,b,c,d,e]
    for bil in angka:
        if (bil%2==0):
            jmlGenap +=1
        if (bil%2!=0):
            jmlGanjil +=1
        if (bil>0):
            jmlPositif +=1
        if (bil<0):
            jmlNegatif +=1

    print(jmlGenap, "Angka Genap")
    print(jmlGanjil, "Angka Ganjil")
    print(jmlPositif, "Angka Positif")
    print(jmlNegatif, "Angka Negatif")