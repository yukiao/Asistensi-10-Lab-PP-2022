
try:
    n=int(input('masukkan nilai n: '))
except:
    print('error')
# A={0,1,1,2,3,5,8,13,...,}
print(n)
first = 0
second = 1

# Perbaikan
# input = 4.5
# output = inputan tidak valid

#input = -1
# output = inputan tidak valid

#inputan mulai dari 1




i = 0

while i < n:
    print(first, end=" ")
    temp = first + second
    first = second
    second = temp

    i = i + 1 








