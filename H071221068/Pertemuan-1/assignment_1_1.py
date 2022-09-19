import math 


h=float(input("Masukkan Tinggi Menara (h) :"))
a=float(input("Masukkan Sudut Elevasi Belakang Kapal (a) :"))

if(a > 90):
    print("Silahkan Masukkan Nilai a kurang atau sama dengan 90")
else:
    b=float(input("Masukkan Sudut Elevasi Depan Kapal (b) :"))

    if(b > a):
        print("Silahkan Masukkan Nilai b kurang dari Nilai a ")
    else:

        b = math.radians(b)
        a = math.radians(a)

        #cari panjang belakang kapal ke menara, misal ac
        # tan a = depan / samping
        # samping = h
        
       
        ac = math.tan(a) * h

        #cari panjang depan kapal ke menara, misal bc
        # tan b = depan / samping
        # samping = h

        bc = math.tan(b) * h

        # jadi panjang kapal ab= ac - bc

        ab = ac - bc
      #  ab=format(ab,'.1f')
        print(round(ab,2),"m")