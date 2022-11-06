
nama_file=input("Masukkan nama file : ")
jumlah_asisten=int(input("Jumlah Asisten: "))

dir_file = r'C:\Users\asran\Downloads\Asistensi fix\{}.txt'.format(nama_file)
try:
    buat_file = open(dir_file, "w")
    judul1 ="+--------------------+------------+----------+\n"
    judul2 ="|Nama                |NIM         |Angkatan  |\n"
    
    # tulis judul ke file
    buat_file.write(judul1)
    buat_file.write(judul2)
    buat_file.write(judul1)

    for i in range(0,jumlah_asisten):
        # Ambil input dari user
        nama = input("Nama: ")
        nim = input("Nim: ")
        angkatan = input("Angkatan: ")
       
        nama=nama.replace(" ","_")
        
        if((int(len(nama)) <= 20) and (int(len(nim)) <= 10) and (int(len(angkatan)) <= 4)):
      
            nama=nama.ljust(20," ")
            nim=nim.ljust(12," ")
            angkatan=angkatan.ljust(10," ")
                
            # format teks
            hasil_input = "|{}|{}|{}|\n".format(nama, nim, angkatan)
            # tulis hasil input ke file
            buat_file.write(hasil_input)

            buat_file.write(judul1)
            buat_file.close()
            print("Berhasil")
        else:
            print("gagal")
            break
   
except:
    print("Gagal")
    


