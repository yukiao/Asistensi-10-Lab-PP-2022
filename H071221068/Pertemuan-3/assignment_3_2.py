try:
    derajat=float(input("Masukkan Derajat :"))
except:
    print("Masukkan Angka 0 - 360")
else:
    if(derajat>=0 and derajat<=360):
        if(derajat>=270):
            #jika derajat lebih dari 270, kurangi 18 jam atau 64800 detik supaya kembali ke  jam 00
            detik=(derajat*10)*24-64800
        else:
            #jika bukan, tambahkan 6 jam atau 21600 detik
            detik=(derajat*10)*24+21600
            
        hh = detik // 3600 
        sisadetik = detik % 3600
        mm = sisadetik // 60
        ss = sisadetik % 60

        if(hh>=5 and hh<10):
            print("Selamat Pagi")
        elif(hh>=10 and hh<15):
            print("Selamat Siang")
        elif(hh>=15 and hh<18):
            print("Selamat Sore")
        elif(hh>=18 and hh<19):
            print("Selamat Petang")
        else:
            print("Selamat Malam")
            
        print("%02i:%02i:%02i" % (hh, mm, ss))
    else:
        print("Masukkan Angka 0 - 360")