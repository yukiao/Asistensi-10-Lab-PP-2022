try :
    c = input()
    d = input()
    with open (c+'.txt', 'r') as file :
         a =file.read()

    with open (d+'.txt', 'w') as file :
        file.write(a)

    print ('Berhasil')

except :
    print ('Gagal')