nama_file = input('Masukkan nama file: ')
nama_salinan = input('Masukkan nama file salinan: ')

try:
    with open (f"{nama_file}.txt", 'w+') as file:
        file.write('''Baris pertama
Baris kedua
Dan seterusnya...''')

    with open(f"{nama_file}.txt", 'r') as file:
        salinan = file.read()
    
    with open(f"{nama_salinan}.txt", 'w') as file2:
        file2.write(salinan)
        print('Berhasil')
except:
    print('Gagal')