

def pergerakan_robot (i,x,y):

    if i == 'R':
        x=x+1
    elif i == 'D':
        y=y-1
    elif i == 'U':
        y=y + 1
    elif i == 'L':
        x= x-1 
    return(x,y)



y=0
x=0

i=0

while True:
    s=input()
    if s =='END':
     break
    if i==0:
    
    
        print(x,y)
    

    for i in s :
        a,b= pergerakan_robot (i,x,y)
        if a == x and b == y :
            continue
        x=a
        y=b
        print(x,y)




    
                


