waktu= int(input("maasukan detik : "))

jam   = (waktu//3600)
menit = (waktu%3600)//(60)
detik = (waktu%3600)%(60)
if menit < 10 and detik < 10 and jam <10 : 
    print (f'0{jam} : 0{menit} : 0{detik}')
elif jam < 10 and menit < 10 :
    print (f'0{jam} : {menit} : 0{detik}')
elif jam < 10 and detik < 10 :
    print (f'0{jam} : {menit} : 0{detik}')
elif menit < 10 and detik < 10 :
    print (f'{jam} : 0{menit} : 0{detik}')
elif detik < 10 : 
    print (f'{jam} : {menit} : 0{detik}')
elif menit < 10 : 
    print (f'{jam} : 0{menit} : {detik}')
elif jam < 10 : 
    print (f'0{jam} : {menit} : {detik}')
else :
    print (f'{jam} : {menit} : {detik}')