print("Selamat datang untuk memulai silahkan input data anda")
nama=input("Input nama: ")
umur=input("Input umur: ")
alamat=input("Input alamat: ")

data_diri = {
    'nama': nama,
    'umur': umur,
    "alamat": alamat
}

print("=================================================")
while True:
    
    print("Selamat datang {} silahkan pilih opsi".format(data_diri.get('nama')))
    print("=================================================")
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("=================================================")
    opsi=input("Input opsi: ")
    print("=================================================")

    if(opsi=="1"):
        print("Data anda adalah")
        print("Nama: {}".format(data_diri.get('nama')))
        print("Umur: {}".format(data_diri.get('umur')))
        print("Alamat: {}".format(data_diri.get('alamat')))
        print("=================================================")
    elif(opsi=="2"):
        nama_baru=input("Silahkan Input nama baru:")
        data_diri['nama']=nama_baru
        print("Data anda sukses di perbarui")
        print("=================================================")
    elif(opsi=="3"):
        umur_baru=input("Silahkan Input Umur baru:")
        data_diri['umur']=umur_baru
        print("Data anda sukses di perbarui")
        print("=================================================")
    elif(opsi=="4"):
        alamat_baru=input("Silahkan Input Alamat baru:")
        data_diri['alamat']=alamat_baru
        print("Data anda sukses di perbarui")
        print("=================================================")
    elif(opsi=="5"):
        print("Selamat Tinggal {}".format(data_diri.get('nama')))
        break