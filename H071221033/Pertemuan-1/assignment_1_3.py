nilai = input("Rata-rata pemakaian listrik harian : ")
tarif = 1325
Wh = float(nilai)

harian = float(Wh / 1000)
bulanan = float(harian * 30)
harga = int(bulanan * tarif)

print("Jumlah tagihan listrik bulanan: Rp. {:.2f}".format(harga))