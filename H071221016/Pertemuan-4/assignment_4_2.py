try:
    def hitung_FPB(x,y):
       if x > y:
        smaller = y
       else:
        smaller = x
       for i in range(1,smaller+1):
        if((x % i == 0) and (y % i == 0)):
            fpb = i

       return fpb
    n1= int(input( ))
    n2= int(input( ))
    print(f"FPB ({n1},{n2}) = ",hitung_FPB(n1,n2))      
      
except:
     print("inputan tidak sesuai")
