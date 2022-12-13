try:
    a = input('Masukkan nama file: ') + '.txt'
    b = input('Masukkan nama file salinan: ') + '.txt'
    cek_len= 0 
    with open(a, 'r') as fileasli:
        for x in fileasli:
            if len (x) > cek_len:
                cek_len = len(x)
                
    with open (a, 'r') as fileasli:
        baris = 1
        banyak_baris = len(fileasli.readlines())                                    # cek jumlah baris dgn readlines utk ambil semua baris , disimpan dalam list
       
    with open(a, 'r') as fileasli: 
        copy = open(b, 'w')
        for i in fileasli:
            if baris < banyak_baris :
                teks_baru = f"{i.rstrip():>{cek_len}}\n"                             # rstrip dst untuk ilangin spasi paling belakang
            else :
                teks_baru = f"{i.rstrip():>{cek_len}}"                               # :>{cek_len} biar rata kanan
            copy.write(teks_baru)
            baris += 1                                                               # biar tau skrng baris ke brp dan baris<banyak_baris berfungsi
        copy.close()
    print('Berhasil')

except:
    print('Gagal')