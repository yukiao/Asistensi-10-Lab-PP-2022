data = int(input('Masukkan angka = '))
satuan = 60
detik = int(data)

jam = int(detik / (satuan * satuan ))
detik = int(detik - (satuan * satuan) * jam)

menit = int(detik / satuan)
detik = int (detik - (satuan * menit))

if jam < 10 or menit < 10 or detik < 10:
    print ('0%d:0%d:0%d' % (jam, menit, detik))
else:
    print ('%d:%d:%d' % (jam, menit, detik))