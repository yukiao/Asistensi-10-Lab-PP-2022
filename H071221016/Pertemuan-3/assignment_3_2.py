n=float(input(''))
jam=6
menit=0
hari=24*3600
detik=round((n/360)*hari)

while detik>=3600 :
    detik-=3600
    jam+=1

while detik>=60 :
    detik-=60
    menit+=1

jam%=24

if jam<4 :
    print('Selamat Malam')
elif jam<=10 :
    print('Selamat Pagi')
elif jam<=14 :
    print('Selamat Siang')
elif jam<=18 :
    print('Selamat Sore')
elif jam<=24:
    print('Selamat Malam')

    
print('%02d:%02d:%02d'%(jam,menit,detik))