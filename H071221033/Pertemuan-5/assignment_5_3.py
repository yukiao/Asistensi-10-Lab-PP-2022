a = input("Input array ke 1: ").split(" ")
b = input("Input array ke 2: ").split(" ")

set_a = set()
set_b = set()

for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(b)):
    b[i] = int(b[i])
set_a.update(a)
set_b.update(b)

tup_a = tuple(set_a & set_b)

print(f'Terdapat {len(set_a & set_b)} buah duplikat yaitu, {tup_a}')







