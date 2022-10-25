nama_file = input('Masukkan nama file: ')
jumlah_data = int(input('Masukkan jumlah data: '))
data_diri = []
tabel = f"+{'-'*20}+{'-'*10}+{'-'*4}+"

for data in range(jumlah_data):
    nama = input('Masukkan nama: ').ljust(20)
    if len(nama) > 20:
        nama = nama[0:20]
        nama = nama.replace(' ', '_')
    nama = nama[0:len(nama)]
    nama = nama.replace(' ', '_')
    nim = input('Masukkan nim: ')
    angkatan = input('Masukkan angkatan: ')
    data_diri.append({'Nama' : nama,
    'NIM' : nim,
    'Angkatan' : angkatan,})
    
with open(f"{nama_file}.txt", 'w') as file:
    for hasil in data_diri:
            format_tabel = f'''
{tabel}
|{hasil['Nama']}|{hasil['NIM']}|{hasil['Angkatan']}|
{tabel}'''
            file.write(f"{format_tabel}")
            continue
        