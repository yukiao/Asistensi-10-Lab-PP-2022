

nama_file=input('masukkan nama file: ')
nama_salinan=input('masukkan nama file salinan: ')


try:
    with open (f'{nama_file}.txt', 'w+')as file:
        file.write(''' Baris pertama
baris kedua
Dan seterusnya...''')

    with open(f'{nama_file}.txt', 'r') as file:
        salinan=file.read()

    with open(f'{nama_salinan}.txt','w')as file2:
        file2.write(salinan)
        print('berhasil')
except:
    print('gagal')