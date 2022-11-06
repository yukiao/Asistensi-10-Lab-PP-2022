usia_hari = int(input(''))

def myDay(usia_hari):
    tahun = usia_hari // 365
    sisa_tahun = usia_hari % 365
    bulan = sisa_tahun // 30

    hari = 0

    if bulan < 30:
       hari += sisa_tahun % 30
    
    x = (f'{tahun} tahun \n{bulan} bulan \n{hari} hari')
    return x

print (myDay(usia_hari))