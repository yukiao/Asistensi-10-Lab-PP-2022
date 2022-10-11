def format_indonesia(tagihan):
    str_tagihan = str(tagihan)
    separate_decimal = str_tagihan.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    return temp_result + "," + before_decimal

golongan = input('Silahkan memilih golongan = ')
daya = int(input('Masukkan besar daya = '))
pemakaian = int(input('Masukkan jumlah pemakaian = '))

if golongan == 'R1' :
    if daya == 900 :
        tagihan = pemakaian * 1352
        print('Jumlah tagihan anda : ', format_indonesia(tagihan))
    elif daya == 1300 :
        tagihan = pemakaian * 1444.70
        print('Jumlah tagihan anda : ', format_indonesia(tagihan))
    elif daya == 2200 :
        tagihan = pemakaian * 1444.70
        print('Jumlah tagihan anda : ', format_indonesia(tagihan))
elif golongan == 'R2' and daya >= 3500 <= 5500 :
    tagihan = pemakaian * 1699.53
    print('Jumlah tagihan anda : ', format_indonesia(tagihan))
elif golongan == 'R3' and daya >= 6600 :
    tagihan = pemakaian * 1699.53
    print('Jumlah tagihan anda : ', format_indonesia(tagihan))
elif golongan == 'B2' and daya >= 6600 <= 200000 :
    tagihan = pemakaian * 1444.70
    print('Jumlah tagihan anda : ', format_indonesia(tagihan))
elif golongan == 'B3' and daya > 200000 :
    tagihan = pemakaian * 1114.74
    print('Jumlah tagihan anda : ', format_indonesia(tagihan))
elif golongan == 'I3' and daya >= 200000 :
    tagihan = pemakaian * 1314.12
    print('Jumlah tagihan anda : ', format_indonesia(tagihan))
elif golongan == 'P1' and daya >= 6600 <= 200000 :
    tagihan = pemakaian * 1523.28
    print('Jumlah tagihan anda : ', format_indonesia(tagihan))
else:
    print('Data yang anda masukkan tidak valid')
