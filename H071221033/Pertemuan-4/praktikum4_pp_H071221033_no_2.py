# program cek bilangan prima
def cekPrima(angka):
    if angka < 2:
        return False
    for i in range(2, angka):
        if angka % i == 0:
            return False
    return True

x = int(input("Masukkan bilangan: "))
x = cekPrima(x)
if x == True:
    print("Ini bilangan prima")
else:
    print("Ini bukan bilangan prima")