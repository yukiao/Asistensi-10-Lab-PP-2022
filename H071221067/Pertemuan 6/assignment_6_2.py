nama_file = input('Masukkan nama file: ')
nama_salinan = input('Masukkan nama file salinan: ')

try:
    with open (f"{nama_file}.txt", 'r') as file:
        salinan = file.readlines()
        salinan[-1] = salinan[-1] + '\n'
        maxchar = 0
        for baris in salinan:
            if maxchar < len(baris):
                maxchar = len(baris)
        
    with open(f"{nama_salinan}.txt", 'w') as file2:
        for baris in salinan:
            file2.write(baris.rjust(maxchar))
        print('Berhasil')
except:
    print('Gagal')