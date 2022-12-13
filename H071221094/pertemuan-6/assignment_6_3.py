



nama_file= input('masukkan nama file: ')
jumlah_data=int(input('masukkan jumlah data: '))
data_diri=[]
tabel= f"{'-'*20}+{'-'*210}+{'-'*4}"

for data in range(jumlah_data):
    nama=input('Masukkan nama: '.ljust(20))
    if len(nama) > 20:
        nama=nama[0:20]
        nama=nama.replace(' ','_')
    nama=nama[0:len(nama)]
    nama=nama.replace(' ','_')
    nim=input('masukkan nim: ')
    angkatan=input('masukkan angkatan: ')
    data_diri.append({'nama' : nama,
    'NIM' : nim,
    'Angkatan': angkatan,})
with open(f"{nama_file}.txt", 'w')as file:
    for hasil in data_diri:
        format_tabel= f'''
{tabel}
|{hasil['nama']}|{hasil['NIM']}|{hasil['Angkatan']}
{tabel}'''
        file.write(f"{format_tabel}")
        continue