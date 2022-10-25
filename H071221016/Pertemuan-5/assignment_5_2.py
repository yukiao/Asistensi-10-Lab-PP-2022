print("\nSelamat datang untuk memulai silahkan input data anda")

nama = input("Input Nama : ")
umur = int(input("Input Umur : "))
alamat = input("Input Alamat : ")

person = {
"Nama": nama, 
"Umur": umur,
"Alamat": alamat 
}

def profil():
    print("========================================================")
    print('Selamat datang', person.get('Nama') ,'silahkan pilih opsi')
    print("========================================================")
profil()

i = 1
while i > 0 :
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")

    print("========================================================")
    option= input("Input opsi : ")
    print("========================================================")

    try :
        option = int(option)
    except :
        print("Inputan salah")
    
    
    match (option):
        case(1):
            print("Data anda adalah")
            print('Nama :', person.get('Nama'))
            print('Umur :', person.get('Umur'))
            print('Alamat :', person.get('Alamat'))
            profil()
        case(2):
              nama_baru = input("Silahkan input nama baru : ")
              person['Nama'] = nama_baru
              print("Data anda sukses di perbarui")
              profil()    
        case(3):
            umur_baru = input("Silahkan input umur baru : ")
            person['Umur'] = umur_baru
            print("Data anda sukses di perbarui")
            profil()
        case(4):
            alamat_baru = input("Silahkan input alamat baru : ")
            person['Alamat'] = alamat_baru
            print("Data anda sukses di perbarui")
            profil()   
        case(5):
            print('Selamat Tinggal', person.get('Nama'))
            break