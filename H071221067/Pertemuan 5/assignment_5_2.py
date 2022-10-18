kata = ['Menu', 'Thank You', 'Sukses Mengubah Data', 'Sukses Memasukkan Data']
print(53*"-")
print(f"Selamat datang".center(53))
print(f"Silahkan Input Data Anda Untuk Memulai Program".center(53))
print(53*"-")

inputnama = input('Nama     : ')
inputumur = input('Umur     : ')
inputdomisili = input('Domisili : ')
datadiri = {
    'Nama': inputnama,
    'Umur': inputumur,
    'Domisili': inputdomisili,
}

def menu():
    print(53*"-")
    print(kata[3].center(53))
    print(53*"-")
    print(53*"=")
    print(f"Selamat datang {datadiri['Nama']}".center(53))
    print(f"Silahkan Memilih Opsi Menu".center(53))
    print(53*"=")
    print(53*"-")
    print(kata[0].center(53))
    print(53*"-")
    print('1]. Detail Data')
    print('2]. Ubah Nama')
    print('3]. Ubah Umur')
    print('4]. Ubah Domisili')
    print('5]. Keluar')
    print(53*"=")
    print(53*"-")
    pilihan = int(input('> Opsi : '))

    return pilihan

def detail_data():
    print(53*"=")
    print('Data anda adalah:')
    print(f"Nama    : {datadiri['Nama']}")
    print(f"Umur    : {datadiri['Umur']}")
    print(f"Domisili: {datadiri['Domisili']}")

def ubah_nama():
    print(53*"-")
    inputnama = input('Silahkan Input Nama Baru: ')
    datadiri['Nama'] = inputnama
    print(53*"-")
    print(kata[2].center(53))
    print(53*"-")

def ubah_umur():
    print(53*"-")
    inputumur = input('Silahkan Input Umur Baru: ')
    datadiri['Umur'] = inputumur
    print(53*"-")
    print(kata[2].center(53))
    print(53*"-")

def ubah_domisili():
    print(53*"-")
    inputdomisili = input('Silahkan Input Domisili Baru: ')
    datadiri['Domisili'] = inputdomisili
    print(53*"-")
    print(kata[2].center(53))
    print(53*"-")

while True:
    pilihan = menu()

    if pilihan == 1:
        jalankan = detail_data()
    elif pilihan == 2:
        jalankan = ubah_nama()
    elif pilihan == 3:
        jalankan = ubah_umur()
    elif pilihan == 4:
        jalankan = ubah_domisili()
    elif pilihan == 5:
        print(53*"-")
        print(kata[1].center(53))
        print(53*"-")
        break
    else:
        continue