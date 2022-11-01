data = int(input('Masukkan angka = '))
satuan = 60
detik = (data)

jam = int(detik / (satuan * satuan ))
detik = int(detik - (satuan * satuan) * jam)

menit = int(detik / satuan)
detik = int(detik - (satuan * menit))

print('%02d:%02d:%02d' % (jam, menit, detik))