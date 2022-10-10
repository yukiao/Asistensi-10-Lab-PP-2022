#MENGHITUNG FPB DENGAN FUNCTION

def getFPB(x, y):
# memilih bilangan yang paling kecil
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            fpb = i
            
    return fpb

# hilangkan tanda # untuk meminta inputan dari user
try:
    num1 = int(input("Masukkan Bilangan Pertama ="))
    num2 = int(input("Masukkan Bilangan Kedua ="))
    
except:
    print("Masukkan bilangan integer ")
else:
    if(num1>0 and num2>0):
        print("FPB({}, {})=".format(num1,num2), getFPB(num1, num2))
    else:
        print("Masukkan bilangan integer Positif")