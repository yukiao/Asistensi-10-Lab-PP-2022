harga_barang = int(input('Masukkan Harga Barang: '))
nilai_uang = int(input('Masukan Nilai Uang: '))
kembalian = (nilai_uang - harga_barang)
a = [100000 , 50000 , 20000 , 10000 , 5000 , 2000 , 1000]

if nilai_uang < harga_barang:
    print('Uang Tidak Cukup')
else:
  for x in range (0,7):
      i = 0
      while kembalian >= a[x]:
          kembalian = kembalian - a[x]
          i = i+1
      uang = f'{a[x]:_}'
      b = uang.replace('_','.')
      print('%d uang Rp. %s'%(i,b))





