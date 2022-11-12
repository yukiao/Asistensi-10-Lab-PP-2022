from os import stat, system

class DataDiri:
    def __init__(self, nim, nama, age, isMale):
        self.nim = nim
        self.nama = nama
        self.age = age
        self.isMale = isMale
    
    def getNim(self):
        return self.nim
    def getNama(self):
        return self.nama
    def getAge(self):
        return self.age
    def getGender(self):
        if(self.isMale==1):
            jk="Pria"
        else:
            jk="Wanita"
        return jk 
    def setNim(self, nim):
        self.nim = nim
    def setNama(self, nama):
        self.nama = nama
    def setAge(self, age):
        self.age = age
    def setGender(self, isMale):
        self.isMale = isMale

def menu():
    system('cls')
    print('Menu Aplikasi Biodata                ')
    print('=====================================')
    print('| 1. Tambah Biodata                 |')
    print('| 2. Tampil Biodata                 |')
    print('| 3. Edit Biodata                   |')
    print('| 4. Hapus Biodata                  |')
    print('| 0. Keluar                         |')
    print('=====================================')
    pilih = input("Masukkan Menu : ")


    if pilih == '1':
        tambah()
    elif pilih == '2':
        lihat()
    elif pilih == '3':
        edit()
    elif pilih == '4':
        hapus()
    elif pilih == '0':
        selesai()
    else:
        tidak = input('Menu Tidak Ada ')
        system('cls')
        menu()

            
def tambah():
    system('cls')
    nim = input("Masukan NIM : ")
    nama = input("Masukan Nama : ")
    umur = int(input("Masukan Umur : "))
    def kel():
        jeniskelamin = int(input("Masukkan Jenis Kelamin [1=Pria, 0=Wanita] :"))
        if(jeniskelamin!=1 and jeniskelamin!=0):
            print ('Input Salah')
            kel()
        else:
            return jeniskelamin
                    
    jeniskelamin=kel()
    mahasiswa = DataDiri(nim,nama, umur, jeniskelamin)
    Daftar_Mahasiswa[nim] = mahasiswa
    print('=====================================')
    print ('Data Tersimpan'.center(40))
    print('=====================================')
    print("")
    kembali = input('Kembali ke menu [tekan enter]')
    menu()

def hapus():
    system('cls')
    nim=input("Masukan NIM : ")
    if(nim in Daftar_Mahasiswa):
        del Daftar_Mahasiswa[nim]
        print('=====================================')
        print('Data Berhasil Dihapus'.center(40))
        print('=====================================')
    else:
        print("Data Tidak Ditemukan")
        
    print("")
    kembali = input('Kembali ke menu [tekan enter]')
    menu()   

def lihat():
    system('cls')
    print()
    if(int(len(Daftar_Mahasiswa))==0):
        print("Data tidak ditemukan")
    else:
        for i in Daftar_Mahasiswa:
            print("NIM : ", Daftar_Mahasiswa[i].getNim())
            print("Nama : ", Daftar_Mahasiswa[i].getNama())
            print("Umur : ", Daftar_Mahasiswa[i].getAge())
            print("Jenis Kelamin : ", Daftar_Mahasiswa[i].getGender())
          
        
    print("")
    kembali = input('Kembali ke menu [tekan enter]')
    menu() 

def edit():
    system('cls')
    print()
    nim = input("Masukan Nim : ")
    if nim in Daftar_Mahasiswa:
        editnama=input("Mau ubah nama (Y/N) :")
        if(editnama.upper()=="Y"):
            namaBaru = input("Masukan Nama Baru : ")
            Daftar_Mahasiswa[nim].setNama(namaBaru)
        print("")    
        editumur=input("Mau ubah umur (Y/N) :")
        if(editumur.upper()=="Y"):
            umurBaru = input("Masukan Umur : ")
            Daftar_Mahasiswa[nim].setAge(umurBaru)
        print("")    
        editjk=input("Mau ubah Jenis Kelamin (Y/N) :")
        if(editjk.upper()=="Y"):
            def kel1():
                jkBaru = int(input("Masukan Jenis Kelamin [1=Pria, 0=Wanita]  : "))
                if(jkBaru!=1 and jkBaru!=0):
                    print ('Input Salah')
                    kel1()
                else:
                    Daftar_Mahasiswa[nim].setGender(jkBaru)
            kel1()
    else:
        print("Data Tidak Ditemukan")
    print("")
    kembali = input('Kembali ke menu [tekan enter]')
    menu() 
def selesai():
    exit()
        
Daftar_Mahasiswa = {}
menu()