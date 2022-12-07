import os
import re

class DataDiri:
    def __init__(self,nama,email,password):
        self.nama = nama
        self.email = email
        self.password = password

    def getNama(self):
        return self.nama
    def getEmail(self):
        return self.email
    def getPassword(self):
        return self.password 
    def setNama(self, nama):
        self.nama = nama
    def setEmail(self, email):
        self.email = email
    def setPassword(self, password):
        self.password = password

def menu():
    print('Selamat Datang Silahkan Pilih Opsi Anda')
    print('1. Detail Anda')
    print('2. Ubah Nama')
    print('3. Jumlah Data Pada File')
    print('4. Save Data pada File')
    print('5. Buat Data Baru')
    print('6. Keluar')
    pilih = input("Silahkan Pilih Opsi Anda : ")


    if pilih == '1':
        lihat() 
    elif pilih == '2':
        edit()
    elif pilih == '3':
        jumlahData()
    elif pilih == '4':
        saveData()
    elif pilih == '5':
        tambah()
    elif pilih == '6':
        selesai()
    else:
        tidak = input('Menu Tidak Ada ')
        menu()

garis='=' * 70

def lihat():
    if(int(len(Daftar_Mahasiswa))==0):
        print(garis)
        print("Data saat ini kosong")
        print(garis)
    else:
        for i in Daftar_Mahasiswa:
            print(garis)
            print("Data anda adalah")
            print("Nama : ", Daftar_Mahasiswa[i].getNama())
            print("Email : ", Daftar_Mahasiswa[i].getEmail())
            print("Password : ", Daftar_Mahasiswa[i].getPassword())
            print(garis)
    menu() 

def edit():
    if(int(len(Daftar_Mahasiswa))==0):
        print(garis)
        print("Data saat ini kosong")
        print(garis)
    else:
        for i in Daftar_Mahasiswa:
            nama=Daftar_Mahasiswa[i].getNama()

        print(garis)
        namaBaru=input("Silahkan Input Nama Baru : ")
        Daftar_Mahasiswa[nama].setNama(namaBaru)
        print(garis)
    menu()

def jumlahData():
    print(garis)
    nama_file=input("Masukkan nama file : ")
    dir_file = r'D:\APLIKASI\PEKAN 14 (PRAK)\{}.txt'.format(nama_file)
    try:
        f = open(dir_file, "r")
        count=0
        for x in f:
            count+=1 
        jml=(count - 3)/4
        f.close()
        print("Jumlah data pada file : {} data".format(int(jml)))
        print(garis)
    except:
        print(garis)
        print('File {}.txt tidak ada'.format(nama_file))
        print(garis)
    menu()

def saveData():
    garis='=' * 70
    if(int(len(Daftar_Mahasiswa))==0):
        print(garis)
        print("Data saat ini kosong")
        print(garis)
    else:
        print(garis)
        nama_file=input("Masukkan nama file : ") + '.txt'
        cekfile=os.path.isfile(nama_file)


        if(cekfile==False):

            buat_file = open(nama_file, "w")
            garis='+=====================================\n'
            judul="Data yang tersimpan\n"
            buat_file.write(garis)
            buat_file.write(judul)
            buat_file.write(garis)
            for i in Daftar_Mahasiswa:

                hasil_input="|Nama : {}\n".format(Daftar_Mahasiswa[i].getNama())
                hasil_input1="|Email : {}\n".format(Daftar_Mahasiswa[i].getEmail())
                hasil_input2="|Password : {}\n".format(Daftar_Mahasiswa[i].getPassword())
                buat_file.write(hasil_input)
                buat_file.write(hasil_input1)
                buat_file.write(hasil_input2)
                buat_file.write(garis)
            buat_file.close()
            print("Berhasil")
            print(garis)
            Daftar_Mahasiswa.clear()
        else:

            buat_file = open(nama_file, "a")
            garis='+=====================================\n'
            for i in Daftar_Mahasiswa:

                hasil_input="|Nama : {}\n".format(Daftar_Mahasiswa[i].getNama())
                hasil_input1="|Email : {}\n".format(Daftar_Mahasiswa[i].getEmail())
                hasil_input2="|Password : {}\n".format(Daftar_Mahasiswa[i].getPassword())
                buat_file.write(hasil_input)
                buat_file.write(hasil_input1)
                buat_file.write(hasil_input2)
                buat_file.write(garis)
            buat_file.close()
            print("Berhasil")
            print(garis)
            Daftar_Mahasiswa.clear()
    menu()

def checkemail():

    regex = r'\b[a-z0-9]+@student.unhas.ac.id'
    email = input("Silahkan Masukkan Email Anda : ")
    cek=re.fullmatch(regex, email)
    if(cek==None):
        print(garis)
        print("Email yang anda masukkan salah")
        print(garis)
        return checkemail()

    else:
        return email   

def checkpassword():
        capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        smallalphabets="abcdefghijklmnopqrstuvwxyz"
        digits="0123456789"

        password = input("Silahkan Masukkan Password Anda : ")
        if (len(password) >= 8 and len(password) <= 20):
            l=0
            u=0
            d=0
            for i in password:

                if (i in smallalphabets):
                    l+=1           
                if (i in capitalalphabets):
                    u+=1           
                if (i in digits):
                    d+=1        

            if (l>=1 and u>=1 and d>=1 and l+u+d==len(password)):
                return password
            else:
                print(garis)
                print("Password yang anda masukkan terlalu lemah, \n Gunakan minimal 1 huruf kapital, huruf kecil, dan angka")    
                print(garis)
                return checkpassword()
        else:
            print(garis)
            print("Password harus memiliki Panjang 8 - 20 karakter")
            print(garis)
            return checkpassword()

def tambah():
    Daftar_Mahasiswa.clear()
    print(garis)
    nama = input("Silahkan Masukkan Nama Anda : ")
    email=checkemail()
    password=checkpassword()

    print(garis)

    mahasiswa = DataDiri(nama,email,password)
    Daftar_Mahasiswa[nama] = mahasiswa
    menu()

def selesai():
    print("Sampai jumpa lagi")
    exit()

Daftar_Mahasiswa = {}
menu()