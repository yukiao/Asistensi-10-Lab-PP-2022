a = input('')
b = input('')

try:
    with open(f'{a}.txt') as file:
        file_array = file.readlines()
        file_array[-1] = file_array[-1] + '\n'
        file_max = 0
        for row in file_array:
            file_len = len(row)
            if file_len > file_max:
                file_max = file_len

    with open(f'{b}.txt','w') as files:
        for j in range (len(file_array)):
            files.write(file_array[j].rjust(file_max))
        print('Berhasil')
except:
    print('Gagal')
