print("Program Konversi Detik Ke Jam")

detik=int(input("masukkan waktu dalam satuan detik : "))
hh = detik // 3600
sisadetik = detik % 3600
mm = sisadetik // 60
ss = sisadetik % 60

print("%02i:%02i:%02i" % (hh, mm, ss))