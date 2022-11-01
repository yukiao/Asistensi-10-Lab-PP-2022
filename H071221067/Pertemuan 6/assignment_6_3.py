nama_file = input('Masukkan nama file: ')
jumlah_data = int(input('Masukkan jumlah data: '))
data_diri = []
tabel = f"+{'-'*20}+{'-'*10}+{'-'*10}+"

for data in range(jumlah_data):
    nama = input('Masukkan nama: ')
    nama = nama.replace(' ', '_').ljust(20)
    if len(nama) > 20:
        nama = nama[0:20]
        nama = nama.replace(' ', '_')
    nama = nama[0:len(nama)]
    nim = input('Masukkan nim: ')
    angkatan = input('Masukkan angkatan: ').center(10)
    data_diri.append({'Nama' : nama,
    'NIM' : nim,
    'Angkatan' : angkatan,})
    
with open(f"{nama_file}.txt", 'w') as file:
    file.write(f'''+--------------------+----------+----------+
| Nama               | NIM      | Angkatan |
+--------------------+----------+----------+''')
    for hasil in data_diri:
            format_tabel = f'''
|{hasil['Nama']}|{hasil['NIM']}|{hasil['Angkatan']}|'''
            file.write(f"{format_tabel}")
            continue
    file.write(f"\n{tabel}")     