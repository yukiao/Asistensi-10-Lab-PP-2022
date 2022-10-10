def faktorial(angka):
    if angka == 1:
        return angka
    else:
        return angka * faktorial(angka - 1)

bilangan = int(input('Masukkan angka: '))
if bilangan == 0:
    print('1')
elif bilangan < 0:
    bilangan = int(input('Masukkan angka (harus lebih dari 0): '))
    if bilangan == 0:
        print('1')
    else:
        print(faktorial(bilangan))
else:
    print(faktorial(bilangan))