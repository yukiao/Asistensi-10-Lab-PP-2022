nama = input("Masukkan nama: ")
gaji_pokok = float(input("Masukkan gaji pokok: "))
total_penjualan = float(input("Masukkan total penjualan: "))

total_gaji = total_penjualan*(15/100) + gaji_pokok
print ("TOTAL =", "$", round(total_gaji, 2))