from math import floor
print("====================================")
print("    PROGRAM MENGHITUNG KEMBALIAN    ")
print("====================================")

harga_barang = int(input(''))
nilai_uang = int(input(''))
x = int(nilai_uang - harga_barang) # x = kembalian

seratusribu = 0
limapuluhribu = 0
duapuluhribu = 0
sepuluhribu = 0
limaribu = 0
duaribu = 0
seribu = 0

if x == 0 :
    print("Tidak ada kembalian")
elif nilai_uang < harga_barang:
    print("Uang anda tidak cukup")
else:
        y = floor(x/100000)                                             # floor utk pembulatan ke bawah(lantai)
        seratusribu = seratusribu + y                                   # misal: c = 102.000 -> d = 1,02 = 1 -> seratusribu = 0+1 = 1
        x = x%100000     
                                                          
        y = floor(x/50000)
        limapuluhribu = limapuluhribu + y
        x = x%50000
    
        y = floor(x/20000)
        duapuluhribu = duapuluhribu + y
        x = x%20000
    
        y = floor(x/10000)
        sepuluhribu = sepuluhribu + y
        x = x%10000
   
        y = floor(x/5000)
        limaribu = limaribu + y
        x = x%5000
    
        y = floor(x/2000)
        duaribu = duaribu + y
        x = x%2000
   
        y = floor(x/1000)
        seribu = seribu + y
        x = x%1000
        print(seratusribu, "uang Rp. 100.000")
        print(limapuluhribu, "uang Rp. 50.000")
        print(duapuluhribu, "uang Rp. 20.000")
        print(sepuluhribu, "uang Rp. 10.000")
        print(limaribu, "uang Rp. 5.000")
        print(duaribu, "uang Rp. 2.000")
        print(seribu, "uang Rp. 1.000")