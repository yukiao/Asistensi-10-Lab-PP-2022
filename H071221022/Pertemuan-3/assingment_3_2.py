n = float(input())
if n >= 0 and n <= 360 :
    waktu = n*240 
    jam = waktu/3600
    menit = (waktu%3600)/60
    detik = (menit*60)-(int(menit)*60)
    jam = int(jam) + 6
    if jam >= 24 : 
        jam = jam-24
    detik = int(detik)
    menit = int(menit)
    jam = int(jam)
    if jam >= 12 and jam < 15 : 
        print ("Selamat Siang")
    elif jam >= 15 and jam < 18: 
        print ("Selamat Sore")
    elif jam >= 18 and jam <= 23: 
        print ("Selamat Malam")
    else : 
        print ("Selamat Pagi")
    
    # if menit < 10 and detik < 10 and jam <10 : 
    #     print (f'0{jam} : 0{menit} : 0{detik}')
    # elif jam < 10 and menit < 10 :
    #     print (f'0{jam} : 0{menit} : {detik}')
    # elif jam < 10 and detik < 10 :
    #     print (f'0{jam} : {menit} : 0{detik}')
    # elif menit < 10 and detik < 10 :
    #     print (f'{jam} : 0{menit} : 0{detik}')
    # elif detik < 10 : 
    #     print (f'{jam} : {menit} : 0{detik}')
    # elif menit < 10 : 
    #     print (f'{jam} : 0{menit} : {detik}')
    # elif jam < 10 : 
    #     print (f'0{jam} : {menit} : {detik}')
    # else :
    #     print (f'{jam} : {menit} : {detik}')

    print (f"{jam :02d} : {menit :02d} : {detik :02d}")

else : 
    print ("keluar dari rentang sudut")