nama_file = input() + ".txt"
x = int(input())

file = open(nama_file, "w")


try:
    file.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")
    file.write("|" + " Nama" + " "*17 + "|" + " NIM" + " "*8 + "|" + " Angkatan" + " " + "|" + "\n")
    file.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")

    for i in range(x):
        nama = input().replace(" ","_")
        if len(nama) <= 20:
          
            nim = input()
            angkatan = input()
    
            file.write("|" + " " + nama + " "*(22 - (len(nama)+1)) + "| " + nim + " | " + angkatan + " "*5 + "|" + "\n")
        else:
            print('Gagal')
            break
    if len(nama) <= 20:

        file.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+")
    
        print("Berhasil")
except:
    print("Gagal")
    
file.close()
            