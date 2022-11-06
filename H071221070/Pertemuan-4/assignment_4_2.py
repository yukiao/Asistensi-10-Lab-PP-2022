def getFPB(a,b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller +1):
        if ((a%i==0) and (b%i==0)):
            fpb=i
    return fpb

try:
    a = int(input(''))
    b = int(input(''))
    print ('FPB ({}, {}) = {}'.format(a , b , getFPB(a,b)))
except:
    print('Input Tidak Valid')