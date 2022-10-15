#program mencari FPB


bilangan_a=int(input('\n'))
bilangan_b=int(input())

def mencari_FPB(bilangan_a,bilangan_b):
    if bilangan_a > bilangan_b:
        bilangan_terkecil = bilangan_b
    else:
        bilangan_terkecil = bilangan_a

    for i in range (1,bilangan_terkecil+1):
        if(bilangan_a%i == 0) and (bilangan_b % i == 0):
            fpb=i
    return fpb

print(f"FPB({bilangan_a},{bilangan_b})= { mencari_FPB ( bilangan_a , bilangan_b )}")        
