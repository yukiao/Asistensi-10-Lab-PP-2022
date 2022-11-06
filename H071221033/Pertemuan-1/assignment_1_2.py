detik = int(input("Masukkan jumlah detik : "))

jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
Detik = sisa_detik % 60

print("%02d:%02d:%02d" % (jam, menit, Detik))