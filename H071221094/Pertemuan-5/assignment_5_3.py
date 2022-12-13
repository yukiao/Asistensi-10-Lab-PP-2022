




from multiprocessing.reduction import duplicate


array1=[]
array2=[]

array1=input('masukkan array pertama\n ').split(' ')
array2=input('masukkan array kedua\n').split(' ')

baris1=set(array1)
baris2=set(array2)
duplicate=baris1 & baris2
duplicate=list(duplicate)
duplicate.sort()
hasil= ','.join(duplicate)
print('____________________________')
print(f'terdapat {len(duplicate)}\n angka yang terduplikasi yaitu angka {hasil}')


