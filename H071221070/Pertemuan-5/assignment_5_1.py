lists_n = [0,0],[0,0]
lists_x = [0,0],[0,0]

for i in range(2):
    for j in range(2):
        n = int(input(f'Input nilai matrix pertama index {i+1},{j+1}:'))
        lists_n[i][j] = n
for i in range(2):
    for j in range(2):
        x = int(input(f'Input nilai matrix kedua index {i+1},{j+1}:'))
        lists_x [i][j] = x

perkalian_1 = (lists_n[0][0])*(lists_x[0][0]) + (lists_n[0][1])*(lists_x[1][0])
perkalian_2 = (lists_n[0][0])*(lists_x[0][1]) + (lists_n[0][1])*(lists_x[1][1])
perkalian_3 = (lists_n[1][0])*(lists_x[0][0]) + (lists_n[1][1])*(lists_x[1][0])
perkalian_4 = (lists_n[1][0])*(lists_x[0][1]) + (lists_n[1][1])*(lists_x[1][1])

print('Hasil perkalian matrix')
print(f'|{lists_n[0][0]}, {lists_n[0][1]}| x |{lists_x[0][0]}, {lists_x[0][1]}| = |{perkalian_1}, {perkalian_2}|')
print(f'|{lists_n[1][0]}, {lists_n[1][1]}|   |{lists_x[1][0]}, {lists_x[1][1]}| = |{perkalian_3}, {perkalian_4}|')