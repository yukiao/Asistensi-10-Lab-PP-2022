a=input("Input Array Ke 1 : ")
b=input("Input Array Ke 2 : ")

a=a.split()
b=b.split()

duplikat=[]
jml=0
for h in a:
    for g in b:
        if(h==g):
            duplikat.append(int(g))
            jml=jml+1
            
duplikat=(str(sorted(duplikat)).replace('[','(')).replace(']',')')

if(jml> 0):
    print("Terdapat {} buah duplikat yaitu {}".format(jml,duplikat))
else:
    print("Tidak terdapat duplikat")

     
