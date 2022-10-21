list1 = []
list2 = []
list1 = input('Input array pertama: ').split(' ')
list2 = input('Input array kedua: ').split(' ')
hasil = []
for i in list1:
    if i in list2:
        if i not in hasil:
            hasil.append(i)

if len(hasil) == 0:
    print(f"Tidak ada duplikat")
else:
    print(f"Terdapat {len(hasil)} angka yang terduplikasi yaitu angka {tuple(hasil)}")