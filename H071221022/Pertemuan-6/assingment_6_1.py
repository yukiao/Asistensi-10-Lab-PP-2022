try : 
    file01 = input()
    isi_file = open(f"{file01}.txt")

    file02 = input()
    if file02 == file01 : 
        file02 = f"{file02}-baru"
    with open(f"{file02}.txt","w") as file2 : 
        file2.write(f"{isi_file.read()}")

    file1 = open(f"{file01}.txt")
    file2 = open(f"{file02}.txt")

    if file1.read() == file2.read() : 
        print ("Berhasil")
    else : 
        print ("Gagal")
    isi_file.close()
    file1.close()
    file2.close()
except : 
    print("Gagal")



        