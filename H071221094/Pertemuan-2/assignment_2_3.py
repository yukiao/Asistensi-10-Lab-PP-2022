try:
    a,b,c,d,e=[int(x) for x in input('masukkan angka=').split()]
except:
    print('inputan tidak valid')
else:
    jumlah_genap=0
    jumlah_ganjil=0
    jumlah_positif=0
    jumlah_negatif=0
    angka=[a,b,c,d,e]
    for bil in angka:
        if (bil%2==0):
            jumlah_genap +=1
        if (bil%2==1):
            jumlah_ganjil +=1
        if(bil<0):
            jumlah_negatif +=1
        if(bil >0):
            jumlah_positif
print(jumlah_ganjil,'angka ganjil')
print(jumlah_genap,'angka genap')
print(jumlah_positif,'angka positif')
print(jumlah_negatif,'angka negatif')