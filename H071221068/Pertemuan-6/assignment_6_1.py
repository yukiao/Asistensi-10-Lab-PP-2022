
asal=input("Masukkan Nama File Asal : ")
tujuan=input("Masukkan Nama File Tujuan : ")
dir_asal = r'C:\Users\asran\Downloads\Asistensi fix\pertemuan 7\{}.txt'.format(asal)
dir_tujuan = r'C:\Users\asran\Downloads\Asistensi fix\pertemuan 7\{}.txt'.format(tujuan)


try:
    #buat file txt
    buat_file = open(dir_asal, "w")
    isi ="Baris Pertama\nBaris Kedua\nDan Seterusnya..."
    #isi file txt sesuai isi diatas
    buat_file.write(isi)
    buat_file.close()
    # menyalin file  
    buat_file2 = open(dir_tujuan, "w")
    for teks in open(dir_asal, "r").readlines():
        buat_file2.write(teks)
        
    buat_file2.close()
    print("Berhasil")
    
except:
    print("Gagal")