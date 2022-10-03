def format_indonesia(nilai):
    after_decimal = str(nilai)
    
    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    return temp_result 
try:
    hb = int(input('masukan harga barang: '))
    uang = int(input('masukan nilai uang: '))
except:
    print("Input Bilangan integer")
else:
    uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    jumlah_pecahan = {}
    sisa = uang-hb
    pembulatan_sisa=round(sisa/1000)*1000
    if((sisa==pembulatan_sisa and pembulatan_sisa!=0) or sisa==0):
        for pecahan in uang_pecahan:
            banyak_pecahan = int(sisa / pecahan)
            sisa = sisa%pecahan
            print(banyak_pecahan,' uang Rp. ',format_indonesia(pecahan))
            
    else:
       print("Tidak dapat menampilkan hasil")
