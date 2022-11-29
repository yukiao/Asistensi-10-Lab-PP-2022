import re 
class Data :
    def __init__(self) :
        self.__nama = 1
        self.__email = 2
        self.__pas = 3
    def setnama (self,x):
        self.__nama = x
    def setemail (self,x):
        self.__email = x
    def setpas (self,x):
        self.__pas = x
    def getnama (self):
        return  self.__nama  
    def getemail (self):
        return self.__email  
    def getpas (self):
        return   self.__pas 
    def hitungdata(self):
        input_nama_file2 = input ("Silahkan masukan file nama file :")
        try :
            file = open (f"{input_nama_file2}.txt")
            list_baris = file.readlines()
            str_baris = " ".join(list_baris)
            x = 0
            tes = r'Nama     :'
            list_baris2 = re.findall(tes, str_baris)
        
            
            return len(list_baris2)
        except :
            print (f"Tidak Terdapat file dengan nama {input_nama_file2}.txt")
            print ("Jumlah Data pada File: 0")
data = Data ()    
while True :
    print ("="*70)
    print ("Selamat Datang Silahkan Pilih Opsi Menu Anda ")
    print ("1. Detail Anda ")
    print ("2. Ubah Nama  ")
    print ("3. Jumlah Data pada File ")
    print ("4. Save Data pada File  ")
    print ("5. Buat Data Baru  ")
    print ("6. Keluar")
    input1 = input("Silahkan Pilih Opsi Anda : ")
    print ("="*70)
    if input1 == "5":
        x = input("Silahkan Masukan Nama Anda : ")
        data.setnama(x)
        import re 
        while True :
            email = input("Silahkan Masukan email Anda : ")
            tes_email = r"[a-z0-9]{1,100}(@student.unhas.ac.id)$"
            match = re.match (tes_email, email )
            if match :
                data.setemail(email)
                break
            else :
                print ("="*70)
                print ("Emai yang ada masukan salah ")
                print ("="*70)
        while True :
            pas = input("Silahkan Masukan Password Anda : ")
            tes_pas = r".{8,20}"
            if re.search (tes_pas, pas ):
                tes2_pas = r"[A-Z]"
                tes3_pas = r"[0-9]"
                tes4_pas = r"[a-z]"
                if re.search(tes2_pas, pas) is None :
                    print ("="*70)
                    print ("Password yang anda masukkan terlalu lemah ")
                    print ("Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka ")
                    print ("="*70)
                elif re.search(tes3_pas, pas) is None :
                    print ("="*70)
                    print ("Password yang anda masukkan terlalu lemah ")
                    print ("Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka ")
                    print ("="*70)
                elif re.search(tes4_pas, pas) is None :
                    print ("="*70)
                    print ("Password yang anda masukkan terlalu lemah ")
                    print ("Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka ")
                    print ("="*70)
                    
                else :
                    data.setpas(pas)
                    break
            else :
                print ("="*70)
                print ("Password Harus Memiliki panjang 8-20 karakter")
                print ("="*70)
            
    elif input1 == "1":
        if data.getnama() == 1 :
            print ("Data saat ini kosong")
        else :
            print ("Data Anda Adalah ")
            print (f"Nama : {data.getnama()}")
            print (f"Email : {data.getemail()}")
            print (f"Password {data.getpas()}")
            
            
    elif input1 == "2":
        if data.getnama() == 1 :
            print ("Data Saat Ini Kosong")
           
        else :
            nama = input("Silahkan Input nama baru :  ")
            data.setnama(nama)
            print ("="*70)
            
    elif input1 == "4":
        if data.getemail () ==2 :
            print ("Data Saat Ini kosong")
        else :
            input_nama_file = input("Silahkan Maukan nama file")
            try :
                file_data = open (f"{input_nama_file}.txt", "x")
                file_data.write ("="*70)
                file_data.write ("\n|Data yang tersimpan\n")
                file_data.write ("="*70)
                file_data.write (f"\n|Nama     : {data.getnama()}" )
                file_data.write(f"\n|Email    : {data.getemail()}" )
                file_data.write(f"\n|Password : {data.getpas()} " )
                file_data.write ("\n")
                file_data.write ("="*70)
            except :
                with open (f"{input_nama_file}.txt", "a") as file_data :
                    file_data.write (f"\n|Nama     : {data.getnama()}" )
                    file_data.write(f"\n|Email    : {data.getemail()}" )
                    file_data.write(f"\n|Password : {data.getpas()} " )
                    file_data.write ("\n")
                    file_data.write ("="*70)
                
            data.setnama(1)
            data.setemail(2)
            data.setpas(3) 
            file_data.close()
            print ("Data berhasil di simpan ")
            
    elif input1 == "3":
        print ("jumlah data adalah : ", data.hitungdata())
    elif input1 == "6":
        print ("Sampai Jumpa Lagi")
        print ("="*70)
        break