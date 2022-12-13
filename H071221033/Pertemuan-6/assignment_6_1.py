a = input("Masukkan nama file yang akan di copy: ") + '.txt'                                        # .txt biar langsung pake extensi gausa ditulis diinputan
b = input("Masukkan nama file setelah di copy: ") + '.txt'

try:
    with open(a, 'r') as file:                                                                      # buka file Latihan dgn mode 'r'ead
        baca = file.read()                                                                          # pake variabel biar nyambung sm bawah                    
except:
    print("Gagal")
else:
    with open(b, 'w') as file:                                                                      # buka file copyan dgn mode 'w'rite
       file.write(baca)                                                                             # perintah buka file yg diatas
    print("Berhasil")