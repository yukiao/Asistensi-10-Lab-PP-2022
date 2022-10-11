def faktorial (x):
    if x >= 2:
        return x * faktorial(x - 1)
    elif 0 <= x < 2:
        return 1
    else:
        return 'Inputan Salah'
    return 2
    
try:
    x = int(input(''))
    print(faktorial(x))
except: 
    print ('Inputan Salah')