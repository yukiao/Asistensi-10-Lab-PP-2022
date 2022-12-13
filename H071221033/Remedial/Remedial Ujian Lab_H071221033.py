import re                                                               # import module re untuk menggunakan regex

password = input("Masukkan password: ")                                 # variabel untuk memasukkan password yang akan diuji kecocokannya
pattern = re.match("^[NPX]{3}[A-Za-z5]{6}[NPX]{3}$", password)          # format pasword yang diinginkan, 3 huruf pertama dan terakhir NPX, 6 huruf ditengah uppercase, lowercase, dan angka 5
if pattern:                                                             # permisalan if untuk cek kecocokan password
    print("Valid")                                                      # jika password yang dimasukkan sesuai dengan pattern, maka akan ter-print Valid
else:                                                                   
    print("Tidak Valid")                                                # jika password tidak sesuai, maka akan ter-print Tidak Valid