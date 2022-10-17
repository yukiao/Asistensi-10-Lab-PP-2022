try:
   def faktorial (nilai) :
    if nilai == 1 :
        return (nilai)
    else :
        return (nilai*faktorial(nilai-1))
   angka = int(input( ))
   print(faktorial(angka))            
except:
    print("inputan tidak sesuai")   