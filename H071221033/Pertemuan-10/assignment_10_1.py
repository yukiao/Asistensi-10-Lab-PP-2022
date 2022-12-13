import re
import os
def menu():
    print('=' * 50)
    print('Selamat Datang Silahkan Pilih Opsi Menu Anda')
    print('1. Detail Anda')
    print('2. Ubah Nama')
    print('3. Jumlah Data pada File')
    print('4. Save Data pada File')
    print('5. Buat Data Baru')
    print('6. Keluar')

data = None

while True:
    menu()
    opsi = input("Silahkan Pilih Opsi Anda: ")
    
    try:
        opsi = int(opsi)
    except:
        print("Inputan salah")
    else:
        match opsi:
            case 1:
                if data == None:
                    print('=' * 50)
                    print('Data Saat Ini Kosong')    
                else:
                    print('Nama: ', data['Nama'])
                    print('Email: ', data['Email'])
                    print('Password: ', data['Password'])
            case 2:
                if data == None:
                    print('=' * 50)
                    print('Data Saat Ini Kosong')
                else:
                    data['Nama'] = input("Nama Baru : ")
            case 3:
                print(50*'=')
                fileName = input("Silahkan masukkan nama file : ") 
                print("Berhasil")
                try:
                    with open(f"{fileName}.txt") as file:
                        data = file.read()
                        total = data.count("@student.unhas.ac.id")
                        print(f"Jumlah data anda adalah : {total} data")
                except:
                    print(f"tidak terdapat file dengan nama {fileName}.txt")
                    print(f"Jumlah data anda adalah : 0 data")
            case 4:
                if data == None:
                    print('=' * 50)
                    print('Data Saat Ini Kosong')
                else:
                    file_name = input("Masukkan Nama File: ") + '.txt'
                    if os.path.exists(file_name):
                        with open(file_name, 'a') as file:
                            file.write(f"\n|Nama\t\t: {data['Nama']}\n")
                            file.write(f"|Email\t\t: {data['Email']}\n")
                            file.write(f"|Password\t: {data['Password']}\n")
                            file.write(f"+"+"=" * 100)
                    else:
                        with open(file_name, 'x') as file:
                            file.write("+"+"=" * 100)
                            file.write(f"\n|Data Yang Tersimpan\n")
                            file.write("+"+"=" * 100)
                            file.write(f"\n|Nama\t\t: {data['Nama']}\n")
                            file.write(f"|Email\t\t: {data['Email']}\n")
                            file.write(f"|Password\t: {data['Password']}\n")
                            file.write("+"+"=" * 100)
                    print("Berhasil")
                    data = None
            case 5:
                data = {
                    "Nama": "" ,
                    "Email": "",
                    "Password": "" 
                }

                print('=' * 50)
                data["Nama"] = input("Silahkan Masukkan Nama Anda: ")
                while True:
                    email = input("Silahkan Masukkan Email Anda: ")
                    if re.fullmatch("^[a-z0-9]{1,}(@student\.unhas\.ac\.id$)", (email)):
                        data["Email"] = email
                        break
                    else:
                        print("Email Yang Anda Masukkan Salah")
                while True:
                    password = input("Silahkan Masukkan Password Anda: ")
                    if re.fullmatch(".{8,20}", (password)):
                        if re.findall("[A-Z]+", (password)) and re.findall("[a-z]+", (password)) and re.findall("[0-9]+", (password)):
                            data["Password"] = password
                            break
                        else:
                            print("Password Yang Anda Masukkan Terlalu Lemah")
                            print("Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka")
                    else:
                        print("Password Harus Memiliki Panjang 8 - 20 Karakter")
            case 6:
                print('Sampai Jumpa Lagi')
                break