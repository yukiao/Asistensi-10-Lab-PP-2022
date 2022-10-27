try :
    print ("Selamat datang untuk memulai silahkan input data anda" )
    dict = {
        "name": "beny"
        ,"umur": 18
        ,"alamt": "makassar"
    }
    dict["nama"] = input("Input nama: ")
    dict["umur"] = input ("Input umur: ")
    dict["alamt"]=input ("Input alamat: ")
    a = dict["nama"]
    b = dict["umur"]
    c = dict["alamt"]
    while True :
        print ('==================================================')
        print (f'Selamat datang {dict["nama"]} silahkan pilih opsi')
        print ('==================================================')
        print ("1. Detail anda")
        print ("2. Ubah Nama")
        print ("3. Ubah Umur")
        print ("4. Ubah Alamat")
        print ("5. Keluar")
        print ('==================================================')
        opsi = input ("Input opsi: ")
        if opsi == "1" : 
            print ("Data anda adalah")
            print (f"Nama: {a}")
            print(f"Umur: {b}")
            print (f"Alamat: {c}")
        elif opsi == "2" : 
            dict["nama"] = input ("Silahkan Input nama baru: ")
            print ("Data anda sukses di diperbarui")
        elif opsi == "3" : 
            dict["umur"] = input ("Silahkan Input umur baru: ")
            print ("Data anda sukses di diperbarui")
        elif opsi == "4" : 
            dict["alamt"] = input ("Silahkan Input alamat baru: ")
            print ("Data anda sukses di diperbarui")
        elif opsi == "5" : 
            print (f"Selamat Tinggal {a}")
            break
        else : 
            print ("tidak ada pada opsi")
except : 
    print ("input anda tidak valid")
        
