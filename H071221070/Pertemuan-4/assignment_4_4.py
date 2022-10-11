n = input('')

def robot(n):
   x = 0
   y = 0
   if n != 'END':
      print ('0 0')
   while n != 'END':
      for i in range(len(n)):
          letter = n[i]

          if letter == 'R':
             x = x+1
             y = y
             print(x,y)
          elif letter == 'L':
             x = x-1
             y = y
             print(x,y)
          elif letter == 'U':
             x = x
             y = y+1
             print(x,y)
          elif letter == 'D':
             x = x
             y = y-1
             print(x,y)
      n = input('')

robot(n)



