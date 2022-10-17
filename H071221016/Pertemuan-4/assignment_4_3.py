h = int(input())

def myday(h):
    tahun = h//365
    sisahari = h%365
    bulan = sisahari// 30
    hari = sisahari % 30
    print(f'{tahun} tahun')
    print(f'{bulan} bulan')
    print(f'{hari} hari')
myday(h)
