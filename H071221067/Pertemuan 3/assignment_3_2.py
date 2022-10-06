suku_pertama = 0
suku_kedua = 1
counter = 0

try:
    suku_ke_n = int(input('Masukkan nilai suku ke n = '))
    while suku_ke_n <= 0:
        suku_ke_n = int(input('Masukkan nilai sukunya harus di atas 0 oi = '))
        if suku_ke_n <= 0:
            print('Batu lu kalau dibilangin')

    while counter < suku_ke_n:
        print(suku_pertama, end=' ')
        bilangan_terakhir = suku_pertama + suku_kedua
        suku_pertama = suku_kedua
        suku_kedua = bilangan_terakhir
        counter = counter + 1
    print()
except:
    print('Inputan harus berupa bilangan bulat positif yang lebih dari 0')