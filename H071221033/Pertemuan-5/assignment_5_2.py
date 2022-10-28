# bikin biodata pake dictionary
print("Selamat datang untuk memulai silakan input data anda")
nama = input("Input nama: ")
umur = int(input("Input umur: "))
alamat = input("Input alamat: ")

data_saya = {"Nama":nama, 
"Umur":umur, 
"Alamat":alamat}

def profil():   
    print(40*"=")
    print("Selamat datang", data_saya.get('Nama'),"silakan pilih opsi")
    print(40*"=")
profil()

x = 1
while x > 0:
    print("1. Detail anda")
    print("2. Ubah nama" )
    print("3. Ubah umur")
    print("4. Ubah alamat")
    print("5. Keluar")
    print("=" * 40)
    opsi = input("Input opsi: ")
    print("=" * 40)
    try :
        opsi = int(opsi)
    except :
        print("Inputan salah")
        break
    else:
        if opsi == 1:
            print("Data anda adalah")
            print('Nama: ', data_saya["Nama"])
            print('Umur: ', data_saya["Umur"])
            print('Alamat: ', data_saya["Alamat"])
            profil()
        elif opsi == 2:
            nama_baru = input("Silakan input nama baru: ")
            data_saya["Nama"] = nama_baru
            print("Data anda sukses diperbarui")
            profil()
        elif opsi == 3:
            umur_baru = input("Silakan input umur baru: ")
            data_saya["Umur"] = umur_baru
            print("Data anda sukses diperbarui")
            profil()
        elif opsi == 4:
            alamat_baru = input("Silakan input alamat baru: ")
            data_saya["Alamat"] = alamat_baru
            print("Data anda sukses diperbarui")
            profil()
        elif opsi == 5:
            print("Selamat tinggal", data_saya["Nama"])
            break