def baris_terpanjang (list) :
    x = 0 
    for i in list : 
        if len(i) > x : 
            x = len(i)
    return x
try :
    file = input ()
    isi_file = open(f"{file}.txt")
    list_baris = isi_file.readlines()

    len_terpanjang = baris_terpanjang (list_baris)

    jumlah_baris = len(list_baris)
    print (jumlah_baris)
    print (len_terpanjang)
    isi_file.close()

    file2 = input ()
    Masukkan = open(f"{file}.txt")
    isi_file2 = open(f"{file2}.txt", "w") 
    for i in range (jumlah_baris) :
        isi_file2.write(Masukkan.readline().rjust(len_terpanjang))
    
    Masukkan.close()
    isi_file2.close()
    print ("Berhasil")
except : 
    print ('Gagal')



