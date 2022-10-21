print('Selamat datang untuk memulai silahkan input data anda')
nama = input('Input nama: ')
umur = int(input('Input umur: '))
alamat = input('Input alamat: ')

dictData = {
    'nama': nama,
    'umur': umur,
    'alamat': alamat,
}

def detail():
    print(f'Data anda adalah\nNama: {dictData["nama"]}\nUmur: {dictData["umur"]}\nAlamat: {dictData["alamat"]}')

def ubah_nama():
    nama_baru = input('Silahkan Input nilai baru: ')
    dictData["nama"] = nama_baru
    print('Data anda sukses diperbarui')

def ubah_umur():
    umur_baru = input('Silahkan Input nilai baru: ')
    dictData["umur"] = umur_baru
    print('Data anda sukses diperbaharui')

def ubah_alamat():
    alamat_baru = input('Silahkan Input nilai baru: ')
    dictData["alamat"] = alamat_baru
    print('Data anda sukses diperbaharui')


while True:
    print('=====================================================')
    print(f'Selamat datang {dictData["nama"]} silahkan pilih opsi')
    print('=====================================================')
    print('1. Detail anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar')
    print('=====================================================')
    opsi = int(input('Input opsi: '))
    print('=====================================================')
    if opsi == 1:
        detail()
    elif opsi == 2:
        ubah_nama()
    elif opsi == 3:
        ubah_umur()
    elif opsi == 4:
        ubah_alamat()
    elif opsi == 5:
        print(f'Selamat Tinggal {dictData["nama"]}')
        break