try:
    x = int(input(' '))
    y = int(input(' '))
    if x<y:
      for i in range(y):
        i+=1
        print(i,end=' ')
        if(i%x == 0):
            print('')
    else:
        print("error")

except:
    print("inputan tidak sesuai")        
        
