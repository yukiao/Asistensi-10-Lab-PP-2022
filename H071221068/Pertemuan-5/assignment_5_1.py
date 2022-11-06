def matrik(x,y,j):
    list0=[]
    list1=[]
    list2=[]
    
    if(j==1):
        ket="pertama"
    elif(j==2):
        ket="kedua"
        
    for i in range(0,x):
        print("Input nilai matriks",ket,"index 1,",i+1,":",end='')
        inp=float(input())
        list1.append(inp)
    list0.append(list1)
    
    for i in range(0,y):
        print("Input nilai matriks",ket,"index 2,",i+1,":",end='')
        inp=float(input())
        list2.append(inp)
    list0.append(list2)
    return list0

def perkalianmatrik(x,y):
    kali=[]
    for a in range(0, len(x)):
        baris=[]
        for b in range(0, len(x[0])):
            total=0
            for c in range(0, len(x)):
                total=total + (x[a][c] * y[c][b])
            baris.append(total)
        kali.append(baris)
    return kali

matrik1 = matrik(2,2,1) # 2,2 ordo matrik dan 1 dibelakang = matrik pertama
matrik2 = matrik(2,2,2) # 2,2 orde matrik dan 2 dibelakang = matrik kedua
kali = perkalianmatrik(matrik1, matrik2)

#ganti [ ] dengan | |
matrik11=(str(matrik1[0]).replace('[','| ')).replace(']',' |')
matrik12=(str(matrik1[1]).replace('[','| ')).replace(']',' |')

matrik21=(str(matrik2[0]).replace('[','| ')).replace(']',' |')
matrik22=(str(matrik2[1]).replace('[','| ')).replace(']',' |')

hasilkali1=(str(kali[0]).replace('[','| ')).replace(']',' |')
hasilkali2=(str(kali[1]).replace('[','| ')).replace(']',' |')


print(matrik11,"x",matrik21,"=",hasilkali1)
print(matrik12," ",matrik22," ",hasilkali2)


    