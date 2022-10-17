#Nur Amalia
#H071221016

bil= str(input())

tot_genap= 0
tot_ganjil= 0
tot_positif= 0
tot_negatif= 0
a, b, c, d, e= bil.split(' ')
cek_angka= a.isnumeric() and b.isnumeric() and c.isnumeric() and d.isnumeric and e.isnumeric()
if cek_angka:
    a= int(a)
    b= int(b)
    c= int(c)
    d= int(d)
    e= int(e)
    if a %2==0:
        tot_genap+=1
    else:
        tot_ganjil+=1
    if b %2==0:
        tot_genap+=1
    else:
        tot_ganjil+=1
    if c %2==0:
        tot_genap+=1
    else:
        tot_ganjil+=1
    if d %2==0:
        tot_genap+=1
    else:
        tot_ganjil+=1
    if e %2==0:
        tot_genap+=1
    else:
        tot_ganjil+=1
    
    if a>0:
        tot_positif+=1
    elif a<0:
        tot_negatif+=1
    if b>0:
        tot_positif+=1
    elif b <0:
        tot_negatif+=1
    if c>0:
        tot_positif+=1
    elif c<0:
        tot_negatif+=1
    if d>0:
        tot_positif+=1
    elif d<0:
        tot_negatif+=1
    if e>0:
        tot_positif+=1 
    elif e<0:
        tot_negatif+=1
    
    print(tot_genap, 'Angka Genap')
    print(tot_ganjil, 'Angka Ganjil')
    print(tot_positif, 'Angka Positif')
    print(tot_negatif, 'Angka Negatif')

else:
    print('Inputan tidak valid')