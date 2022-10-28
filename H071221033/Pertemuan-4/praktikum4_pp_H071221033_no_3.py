# program mengembalikan nilai faktorial
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n*faktorial(n-1)
try:
    n = int(input(''))
    print(faktorial(n))    
except:
    print("Inputan tidak sesuai")