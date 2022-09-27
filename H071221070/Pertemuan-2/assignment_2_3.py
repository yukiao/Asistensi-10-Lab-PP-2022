print ('Masukkan bilangan: ')
print ('===================')

a,b,c,d,e = (input('')) , (input('')), (input('')) , (input('')) , (input(''))
is_string = True

if a.replace("-" , "").isnumeric() and b.replace("-", "").isnumeric() and c.replace("-" , "").isnumeric() and d.replace("-" , "").isnumeric() and e.replace("-" , "").isnumeric():
    is_string = False


if is_string:
    print ('Inputan Tidak Valid')
else:
    a = int(a) ; b = int(b) ; c = int(c) ; d = int(d) ; e = int(e)
    
    genap = 0
    ganjil = 0
    positif = 0
    negatif = 0

    if a%2 == 0:
        genap += 1
    elif a%2 != 0:
        ganjil += 1
    
    if a > 0:
        positif += 1
    elif a < 0:
        negatif += 1


    if b%2 == 0:
        genap += 1
    elif b%2 != 0:
        ganjil += 1
    
    if b > 0:
        positif += 1
    elif b < 0:
        negatif +=1


    if c%2 == 0:
        genap += 1
    elif c%2 != 0:
        ganjil += 1
    
    if c > 0:
        positif += 1
    elif c < 0:
        negatif += 1


    if d%2 == 0:
        genap += 1
    elif d%2 != 0:
        ganjil += 1
    
    if d > 0:
        positif += 1
    elif d < 0:
        negatif += 1


    if e%2 == 0:
        genap += 1
    elif e%2 != 0:
        ganjil += 1
    
    if e > 0:
        positif += 1
    elif e < 0:
        negatif += 1

    print (genap , 'Angka Genap')
    print (ganjil , 'Angka Ganjil')
    print (positif , 'Angka Positif')
    print (negatif , 'Angka Negatif')