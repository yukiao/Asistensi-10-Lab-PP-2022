suku_pertama = 0
suku_kedua = 1
counter = 0

try:
    suku_ke_n = int(input('Masukkan nilai suku ke n = '))

    if suku_ke_n <= 0:
        suku_ke_n = int(input('Masukkan nilai sukunya harus di atas 0 oi = '))
        if suku_ke_n <= 0:
            print('Batu lu kalau dibilangin')
        else:
            while counter < suku_ke_n:
                print(suku_pertama, end=' ')
                bilangan_terakhir = suku_pertama + suku_kedua
                suku_pertama = suku_kedua
                suku_kedua = bilangan_terakhir
                counter = counter + 1
            print()
except:
    suku_ke_n = int(input('Masukkan nilai suku harus lebih dari 0 = '))
    
    if suku_ke_n <= 0:
        print('Batu lu kalau dibilangin')
    else:
        while counter < suku_ke_n:
            print(suku_pertama, end=' ')
            bilangan_terakhir = suku_pertama + suku_kedua
            suku_pertama = suku_kedua
            suku_kedua = bilangan_terakhir
            counter = counter + 1
        print()