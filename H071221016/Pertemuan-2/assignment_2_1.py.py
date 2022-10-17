#NUR AMALIA
#H071221016

print ('Cek Nilai')

try:
    nilai = int(input('Nilai : '))

    if nilai >=90 :
        print(' > Nilai', nilai,  "= 'A' ")
    elif nilai >= 80 :
        print (' > Nilai', nilai, "= 'B' ") 
    elif nilai >= 70 :
        print (' > Nilai', nilai, "= 'C'  ") 
    elif nilai >= 60 :
        print (' > Nilai', nilai, "= 'D' ")
    elif nilai >= 40 :
        print (' > Nilai', nilai, "= 'E' ")
    elif nilai < 40 :
        print (' > Nilai', nilai, "= 'F' ")   

except:
    print("Nilai Tidak Valid")
        
