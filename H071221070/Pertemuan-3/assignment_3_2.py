angka_1 = 0
angka_2 = 1

try:
   x = int(input(''))

   if x == 1:
       print(angka_1)
   elif x == 2:
       print(angka_2)
   elif x > 2:
       print (angka_1 , angka_2 , '' , end='')
       for i in range (2,x):
           n = angka_1 + angka_2
           print(n , '' , end='')
           angka_1 = angka_2
           angka_2 = n
   else:
        print('Inputan Tidak Valid')
except:
    print('Inputan Tidak Valid')