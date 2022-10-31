a = input('')
b = input('')

try:
    with open(f'{a}.txt') as file:
        file_read = file.read()

    with open(f'{b}.txt','w') as files:
        files.write(file_read)
        print('Berhasil')
except:
    print('Gagal')
