x = int(input(''))
y = int(input(''))

for i in range (y):
    if (i + 1) % x == 0:
        print(i + 1)
    else:
        print(i + 1,end = ' ')