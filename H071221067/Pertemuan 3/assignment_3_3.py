def format_indonesia(pecahan):
    str_pecahan = str(pecahan)
    separate_decimal = str_pecahan.split(".")
    after_decimal = separate_decimal[0]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    return temp_result

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

try:
    harga_barang = int(input('Masukkan harga barang: '))
    jumlah_uang = int(input('Masukkan jumlah uang: '))
    
    if harga_barang < 0 or jumlah_uang < 0:
        harga_barang = int(input('Masukkan harga barangnya ga boleh minus ngab: '))
        jumlah_uang = int(input('Masukkan jumlah uang harus lebih dari 0: '))
        if harga_barang < 0 or jumlah_uang < 0:
            print('Batu lu kalau dibilangin')
        else:
            kembalian = jumlah_uang - harga_barang

            if jumlah_uang < harga_barang:
                print('Uang anda tidak mencukupi')
            else:
                for pecahan in pecahan_uang:
                    banyakPecahan = int(kembalian / pecahan)
                    kembalian = kembalian - (pecahan * banyakPecahan)
                    print(banyakPecahan, 'uang Rp.', format_indonesia(pecahan))
except:
    harga_barang = int(input('Masukkan harga yang bener oi: '))
    jumlah_uang = int(input('Masukkan jumlah uang jangan ngacolah: '))

    if harga_barang < 0 or jumlah_uang < 0:
        print('Batu lu kalau dibilangin')
    else:
        kembalian = jumlah_uang - harga_barang

        if jumlah_uang < harga_barang:
            print('Uang anda tidak mencukupi')
        else:
            for pecahan in pecahan_uang:
                banyakPecahan = int(kembalian / pecahan)
                kembalian = kembalian - (pecahan * banyakPecahan)
                print(banyakPecahan, 'uang Rp.', format_indonesia(pecahan))