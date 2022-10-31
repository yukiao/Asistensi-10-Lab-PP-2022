latihan = input('')
jumlah_asisten = int(input(''))
data = []
for i in range(jumlah_asisten):
    nama = input('')
    nama = nama.replace(' ','_')
    nim = input('')
    angkatan = int(input(''))
    dictData = {
        'nama' : nama,
        'nim' : nim,
        'angkatan' : angkatan
    }        
    data.append(dictData)

try:
    with open(f'{latihan}.txt','w') as file:
        file.write(f'+--------------------+-------------+------------+\n')
        file.write(f'| Nama               | NIM         | Angkatan   |\n')
        file.write(f'+--------------------+-------------+------------+\n')
        for i in data:
            file.write(f'|{i["nama"].ljust(20)}|{i["nim"].ljust(10)}   |{i["angkatan"]}        |\n')
        file.write(f'+--------------------+-------------+------------+')
        print('Berhasil')
except:
    print('Gagal')
