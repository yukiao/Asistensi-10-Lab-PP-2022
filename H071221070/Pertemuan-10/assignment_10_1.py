import re

data = []

dictData = {
    'nama' : '',
    'email' : '',
    'password' : ''
}
data.append(dictData)

while True:
    print('='*50)
    print('Selamat Datang Silahkan Pilih Opsi Menu Anda')
    print('1. Detail Anda\n2. Ubah Nama\n3. Jumlah Data pada File\n4. Save Data Baru\n5. Buat Data Baru\n6. Keluar')
    inputOpsi = int(input('Silahkan Pilih Opsi Anda: '))
    print('='*50)

    def passCheckLength(password):
        isLengthMatch = True if 8 <= len(password) <= 20 else False
        return isLengthMatch
    def passCheckSpecial(password):
        isContUpper = 0
        isContLow = 0
        isContNum = 0
        for i in password:
            if (i.isupper()):
                isContUpper += 1
            elif (i.islower()):
                isContLow += 1
            elif (i.isdigit()):
                isContNum += 1
        if (isContUpper >= 1 and isContLow >= 1 and isContNum >= 1):
            return True
        else:
            return False

    if inputOpsi == 5:
        nama = input('Masukkan Nama: ')
        while True:
            email = input('Masukkan Email: ')
            pattern_email = r'^[a-z0-9]{1,}@student.unhas.ac.id$'
            match_email = re.match(pattern_email , email)
            if match_email:
                break
            else:
                print('Email yang Anda Masukkan Salah')
        
        while True:
            password = input('Masukkan Password: ')
            if passCheckLength(password):
                if passCheckSpecial(password):
                    break
                else:
                    print('Password yang anda masukkan terlalu lemah, gunakan minimal huruf kapital, huruf kecil, dan angka')
            else:
                print('Password harus memiliki Panjang 8-20 karakter')
        dictData['nama'] = nama
        dictData['email'] = email
        dictData['password'] = password

    elif inputOpsi == 1:
        if len(dictData['nama']) == 0:
            print('Data saat ini kosong')
        else:
            print(f'Data anda adalah\nNama : {dictData["nama"]}\nEmail : {dictData["email"]}\nPassword : {dictData["password"]}' )

    elif inputOpsi == 2:
        if len(dictData['nama']) != 0:
            namaBaru = input('Silahkan Input Nama Baru: ')
            dictData['nama'] = namaBaru
        else:
            print('Data saat ini kosong')

    elif inputOpsi == 4:
        fileName = input('Silahkan Masukkan Nama File: ')
        if len(dictData['nama']) != 0:
            try:
                with open(f'{fileName}.txt','r') as file1:
                    if len(file1.readlines()) == 0:
                        with open(f'{fileName}.txt','w') as file2:
                            file2.write(f'+==================================================================\n')
                            file2.write(f'|Data yang Tersimpan\n')
                            file2.write(f'+==================================================================\n')
                with open(f'{fileName}.txt','a') as file:
                    for i in data:
                        for j in data:
                            file.write(f'|Nama        : {i["nama"]}\n|Email       : {i["email"]}\n|Password    : {i["password"]}\n')
                            file.write(f'+==================================================================\n')
                        print('Berhasil')
            except:
                print('Gagal')
        else:
            print('Data saat ini kosong')

    elif inputOpsi == 3:
        checkFile = input('Silahkan Masukkan Nama File: ')
        try:
            with open(f'{checkFile}.txt') as baca:
                jumlahData = re.findall(r"@student.unhas.ac.id", baca.read())
            print(f"Jumlah Data pada File : {jumlahData.count('@student.unhas.ac.id')} Data")
        except:
            print(f"Tidak Terdapat File Dengan Nama {checkFile}")
    
    elif inputOpsi== 6:
        print('Sampai Jumpa Lagi')
        break



