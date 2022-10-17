from tkinter import END


x = 0
y = 0
while True :
    inp =  str(input('String : '))
    if inp == "END":
      break
    for i in inp:
       if (i == "R") :
        x = x + 1
        print (x, y)
       elif (i == "L") :
        x = x - 1
        print (x, y)
       elif (i == "U") :
        y = y + 1
        print (x, y)
       elif (i == "D") :
        y = y - 1
        print (x, y)
   
    


