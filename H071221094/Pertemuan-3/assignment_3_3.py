



#menghitung pecahan uang.

harga_barang=int(input('harga barang:'))
nilai_uang=int(input('di bayar:'))
sisa = nilai_uang-harga_barang

uang_pecahan=[100000,50000,20000,10000,5000,2000,1000]

for pecahan in uang_pecahan:
    if nilai_uang>=harga_barang:
        banyak_pecahan=int(sisa/pecahan)
        sisa=sisa-(pecahan * banyak_pecahan)
        print('{} uang Rp.{}'.format(banyak_pecahan,pecahan))

else:
    print('uang tidak cukup')

