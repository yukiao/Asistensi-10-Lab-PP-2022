# praktikum 2 no 2

golongan = input("Pilih golongan : ")
daya = int(input("Masukkan daya : "))
pemakaian = int(input("Masukkan jumlah pemakaian : "))

if golongan == 'R1':
    if daya == 900:
        tagihan = pemakaian * 1352
        print(f"Jumlah tagihan anda : Rp{tagihan:_}".replace('.', ',').replace('_', '.'))
    elif daya == 1300:
        tagihan = pemakaian * 1444.70
        print(f"Jumlah tagihan anda : Rp{tagihan:_}".replace('.', ',').replace('_', '.'))
    elif daya == 2200:
        tagihan = pemakaian * 1444.70
        print(f"Jumlah tagihan anda : Rp{tagihan:_}".replace('.', ',').replace('_', '.'))
elif golongan == 'R2' and 3500 <= daya <= 5500 :
    tagihan = pemakaian * 1699.53
    print(f"Jumlah tagihan anda : Rp{tagihan:_}".replace('.', ',').replace('_', '.'))
elif golongan == 'R3' and daya >= 6600 :
    tagihan = pemakaian * 1699.53
    print(f"Jumlah tagihan anda : Rp{tagihan:_}".replace('.', ',').replace('_', '.'))
elif golongan == 'B2' and 6600 <= daya <= 200000 :
    tagihan = pemakaian * 1444.70
    print(f"Jumlah tagihan anda : Rp{tagihan:_}".replace('.', ',').replace('_', '.'))
elif golongan == 'B3' and daya > 200000 :
    tagihan = pemakaian * 1114.74
    print(f"Jumlah tagihan anda : Rp{tagihan:_}".replace('.', ',').replace('_', '.'))
elif golongan == 'I3' and daya >= 200000 :
    tagihan = pemakaian * 1314.12
    print(f"Jumlah tagihan anda : Rp{tagihan:_}".replace('.', ',').replace('_', '.'))
elif golongan == 'P1' and 6600 <= daya <= 200000 :
    tagihan = pemakaian * 1523.28
    print(f"Jumlah tagihan anda : Rp{tagihan:_}".replace('.', ',').replace('_', '.'))
else:
    print("Data tidak valid")