#program mwnghitung usia seseorang



def myDay():
    data = int(input())
    if data >= 365:
        tahun = data // 365
        sisa= data % 365
        print(f'{tahun} tahun')

    if sisa>=30:
        bulan = sisa // 30
        sisa_hari = sisa% 30
        print(f'{bulan} bulan')

    if sisa_hari >=0:
        hari=sisa_hari 
        print(f'{hari} hari')

myDay()


