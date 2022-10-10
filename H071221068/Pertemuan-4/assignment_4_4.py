def prediksiPosisi(instruction):
    
    for i in range(len(instruction)):
        if instruction[i] in 'UDRL':
            if instruction[i] == 'U':
                y.append(y[-1]+1)
            elif instruction[i] == 'R':
                x.append(x[-1]+1)
            elif instruction[i] == 'L':
                x.append(x[-1]-1)
            elif instruction[i] == 'D':
                y.append(y[-1]-1)
          
            if(hitung==1):
                print(f'{x[0]} {y[0]} \n{x[-1]} {y[-1]}')
            else:
                print(x[-1],y[-1])
        
hitung=0
while True:
    hitung +=1
    if(hitung==1):
        y = [0]
        x = [0]
    else:
        y = [y[-1]]
        x = [x[-1]]
     
    inst=(input())
   
    if (inst.upper()=="END"):
        print("Selesai")
        break  
            
    prediksiPosisi(inst.upper()) 
   
    
        