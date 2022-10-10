#PROGRAM KONVERSI USIA SESEORANG DALAM BENTUK HARI KE TAHUN, BULAN, HARI


def myDay(hari):
    tahun = int(hari/365)
    bulan = int((hari-(tahun*365))/30)
    hari = int(hari - tahun*365 - bulan *30)

    return (f'{tahun} tahun \n{bulan} bulan \n{hari} hari')

try:
    umur_hari = int(input("Usia seseorang dalam hari = "))
except:
    print("Masukkan bilangan integer positif")
else:
    if(umur_hari>0):
        print(myDay(umur_hari))
    else:
        print("Masukkan bilangan integer Positif")
