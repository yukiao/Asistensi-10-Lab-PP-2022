try:
    x = input("Masukkan nilai x : ")
    y = input("Masukkan nilai y: ")

    is_all_numeric = x.isnumeric() and  y.isnumeric()

    if not is_all_numeric:
        raise ValueError ("Silahkan Masukkan Bilanagn Bulat")
    
    else:
        x=int(x)
        y=int(y)
except ValueError as ve:
    print(ve)
except:
    print("Silahkan Masukkan Angka")
else:
    if(x<y):
        for i in range(1,(y+1)):
            if (i%x==0):
                print(i)
            else:  
                print(i,end=" ")
               
    else:
        print("x harus lebih kecil dari y")

    