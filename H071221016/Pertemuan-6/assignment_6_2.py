try :
    c = input()
    b = input()
    max_char=0
    with open (c+'.txt', 'r') as file :
        a = file.readlines()
        a[-1] = a[-1]+'\n'
        for x in a:
          if len(x) >max_char:
            max_char = len(x)
    with open (b+'.txt', 'w') as file :
        for i in (a):
            
            file.write(f"{i:>{max_char}}")
    print ('Berhasil') 
except :
    print ('Gagal')