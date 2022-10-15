#program mencari nilai faktrorial


def hitung_faktorial (n):
    if n >0 :
        return n * hitung_faktorial (n-1)
    
    if n <0 :
        return str('data tidak valid')
    return 1

n=int(input('\n'))

faktorial= hitung_faktorial (n)
print(f'{faktorial}')

