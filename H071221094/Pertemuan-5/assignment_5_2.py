






kata=['Menu','Sukses mengubah data','sukses memasukkan data','Terima kasih']


print(53*'_')
print(f'selamat datang'.center(53))
print(f'silahkan input data anda untuk memulai program'.center(53))
print(53*'_')



memasukkan_nama=input('Nama : ')
memasukkan_umur=input('Umur : ')
memasukkan_alamat=input('Alamat : ')
data_pribadi={
    'Nama': memasukkan_nama,
    'Umur': memasukkan_umur,
    'Alamat': memasukkan_alamat,}


def menu():
    print(40*'_')
    print(kata[3].center(40))
    print(40*'_')
    print(40*'=')
    print(f'Selmat datang {data_pribadi["Nama"]}'.center(40))
    print(f'silahkan memilih opsi menu'.center(40))
    print(40*'=')
    print(40*'_')
    print(kata[0].center(40))
    print(40*'_')
    print('1].Detail data')
    print('2].Ubah Nama')
    print('3].Ubah Umur') 
    print('4].Ubah Alamat')
    print('5].Keluar')
    print(40*'=')
    print(40*'_')
    pilihan=int(input('> Opsi : '))

    return pilihan


def detail_data():
        print(40*'=')
        print('Data anda adalah: ')
        print(f'Nama               :{data_pribadi["Nama"]}')
        print(f'Umur               :{data_pribadi["Umur"]}')
        print(f'Alamat             :{data_pribadi["Alamat"]}')

def mengubah_nama():
        print(40*'-')
        memasukkan_nama=(input('Silahkan Input Nama Baru: '))
        data_pribadi['Nama'] = memasukkan_nama
        print(40*'-')
        print(kata[2].center(40))
        print(40*'-')

def mengubah_umur():
    print(40*'_')
    memasukkan_umur=input('Silahkan Input Umur Baru: ')
    data_pribadi['Umur']=memasukkan_umur
    print(40*'_')
    print(kata[2].center(40))
    print(40*'_')


def mengubah_alamat():
    print(40*'_')
    memasukkan_alamat=(input('Silahkan Input Alamat Baru: '))
    data_pribadi['Alamat']=memasukkan_alamat
    print(40*'_')
    print(kata[2].center(40))
    print(40*'_')

while True:
    pilihan = menu()

    if pilihan ==1:
        dijalankan=detail_data()
    elif pilihan == 2:
        dijalankan=mengubah_nama()
    elif pilihan == 3:
        dijalankan=mengubah_umur()
    elif pilihan == 4:
        dijalankan=mengubah_alamat()
    elif pilihan == 5:
        break   
    else:
        continue
