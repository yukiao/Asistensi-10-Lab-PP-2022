array_1 = {int(array_1)for array_1 in input('Input array ke 1: ').split()}
array_2 = {int(array_2)for array_2 in input('Input array ke 2: ').split()}
duplicate = tuple(array_1 & array_2)
duplicateCount = len(duplicate)
print(f'Terdapat {duplicateCount} buah duplikat yaitu {duplicate}')