golongan = input('Golongan: ')
daya = int(input('Daya: '))
pemakaian = int(input('Pemakaian: '))

if golongan =='R1' and daya == 900:
    tagihan = pemakaian*1352
elif golongan == 'R1' and daya == 1300:
    tagihan = pemakaian*1444.70
elif golongan == 'R1' and daya == 2200:
    tagihan = pemakaian*144.70
elif golongan == 'R2' and 5500 >= daya >= 3500:
    tagihan = pemakaian*1699.53
elif golongan == 'R3' and daya >= 6600:
    tagihan = pemakaian*1699.53
elif golongan == 'B2' and 200000 > daya >= 6600:
    tagihan = pemakaian*1444.70
elif golongan == 'B3' and daya > 200000:
    tagihan = pemakaian*1114.74
elif golongan == 'I3' and daya >= 200000:
    tagihan = pemakaian*1314.12
elif golongan == 'P1' and 200000 >= daya >= 6600:
    tagihan = pemakaian*1523.28
else:
    print ('Data tidak valid.')

total_tagihan = f"{tagihan:_}"
total_tagihan = total_tagihan.replace('.',',')
total_tagihan = total_tagihan.replace('_','.')

print ('jumlah tagihan anda: ' , total_tagihan)