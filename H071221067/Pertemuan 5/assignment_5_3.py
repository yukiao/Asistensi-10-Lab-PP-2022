list1 = []
list2 = []
list1 = input('Input array pertama: ').split(' ')
list2 = input('Input array kedua: ').split(' ')

set1 = set(list1)
set2 = set(list2)
duplicate = set1 & set2
duplicate = list(duplicate)
duplicate.sort()
hasil = ', '.join(duplicate)

print(f"Terdapat {len(duplicate)} angka yang terduplikasi yaitu angka {hasil}")