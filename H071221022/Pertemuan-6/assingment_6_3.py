def penaganan_file(nama_file, x) :
        with open(f"{nama_file}.txt", "w") as file : 
            file.write("+----------------------+------------+----------+\n")
            file.write("| Nama                 | NIM        | Angkatan +\n")
            file.write("+----------------------+------------+----------+\n")
            for i in range (x) : 
                Nama = input ()
                if len(Nama) > 20 :
                    print ("nama tidak boleh 20 karakter")
                    print ("input ulang")
                    penaganan_file(nama_file, x)
                else :
                    nama = Nama.replace (" ", "_")
    
                    nim = input()
                    Angkatan = (input())
                    
                    file.write(f"| {nama.ljust(20)} | {nim.ljust(10)} | {Angkatan.ljust(8)} |\n")
            file.write("+----------------------+------------+----------+\n")
try : 
    nama_file = input()
    x = int (input())

    penaganan_file(nama_file, x)

    print ("Berhasil")
except : 
    print ("Gagal")
