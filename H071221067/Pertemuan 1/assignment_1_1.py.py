pemakaian = int(input('Masukkan angka = '))
# Pemakaian dalam satuan Watt/jam

#Konversi Wh ke kWh
kWh = float(pemakaian / 1000)

tarif = 1325 #/kWh
tagihan = int(kWh * tarif * 30)

print('Jumlah tagihan listrik bulanan: Rp.', tagihan, '.00', sep = '')






