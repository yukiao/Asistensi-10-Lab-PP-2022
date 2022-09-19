#3 Konversi detik ke jam :menit:detikberdasarkan detik

print ("Konversi Detik")

detik = int(input("Masukkan jumlah detik yang ingin dikonversi : "))

jam = detik//3600
sisa = detik%3600
menit = sisa//60
detik = sisa%60

print ("hasil konversi adalah : " , jam,":",menit,":",detik,":",)