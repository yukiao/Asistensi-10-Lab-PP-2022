def prima(angka):
    for i in range (2, int(angka/2)+1):
        if angka % i == 0:
            return False
    return True

bilangan = int(input('Masukkan angka: '))
prima = prima(bilangan)

if bilangan == 0 or bilangan == 1:
    print('Tidak terdefinisikan')
elif bilangan < 0:
    bilangan = int(input('Masukkan angka (harus lebih dari 0): '))
    if bilangan == 0 or 1:
        print('Tidak terdefinisikan')
    elif prima == True:
        print('Ini bilangan prima')
    else:
        print('Ini bukan bilangan prima')
elif prima == True:
    print('Ini bilangan prima')
else:
    print('Ini bukan bilangan prima')