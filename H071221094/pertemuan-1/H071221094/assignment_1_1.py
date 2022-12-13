import math

h=float(input('masukkan tinggi menara: '))
a=float(input('masukkan sudut elevasi belakang kapal: '))

if(a>90):
    print('masukkan nilai a sama atau kurang dari 90')

else:
    b=float(input('masukkan sudut elevasi depan kapal: '))

    if(b>a):
        print('masukkan nilai b kurang dari a')
    else:
      b=math.radians(b)
      a=math.radians(a)
      ac= math.tan(a)*h

      bc=math.tan(b)*h

      ab=ac-bc
      print(round(ab,1), 'm')

