#MENCARI NILAI FAKTORIAL

def hitung_faktorial(n):
    if n == 0:
        return 1
    else:
        return n*hitung_faktorial(n-1)

try:
    n = int(input('Masukkan bilangan bulat = '))    
except:
    print("Masukkan bilangan integer")
else:
    if(n>0):
        print(n,"! =", hitung_faktorial(n))
    else:
        print("Masukkan bilangan integer Positif")
