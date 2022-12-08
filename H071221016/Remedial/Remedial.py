import re
#RegEx
try:
    string_s=str(int(input()))#pada baris ini dibuat variabel yaitu string_s untuk memasukkan inputan yang diinginkan dengan type data string
    data=re.match('^\+62[0-8]{13}$',string_s)
    #didalam variabel data terdapat re.match,match artinya cocok.jadi re.match berfungsi untuk mencocokan pola yang sudah ditentukan.
    # ^\ berfungsi untuk mengecek inputan yang dimulai oleh +62,kemudian [0-8]{13} dia akan menerima inputan berupa angka antara 0 sampai 8 sebanyak 13 angka.
    # $ berfungsi untuk mengecek inputan yang dikhiri oleh angka
    if data :
        print("Valild")
    #kita gunakan pengkondisian jika inputan sesuai dengan pola pada variabel data maka diakan mengeluarkan output "Valid"    
    else:
        print("Tidak Valid")    
    #Apabila inputan tidak sesuai dengan pola pada variabel data maka akan mengeluarkan output "tidak valid" 
except:
    print("Error")  
    #try & except berfungsi untuk menangani error      


