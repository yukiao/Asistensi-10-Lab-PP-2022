total_detik = int(input("Masukkan total detik: "))
jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60
print ("{:0>2d}".format(jam) , ":" , "{:0>2d}".format(menit) , ":" , "{:0>2d}".format(detik))