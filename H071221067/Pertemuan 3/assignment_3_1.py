try:
    x = int(input('Masukkan nilai x = '))
    y = int(input('Masukkan nilai y = '))

    if x <= 0 or y <= 0 or x > y:
        x = int(input('Masukkan nilai yang benerlah = '))
        y = int(input('Masukkan nilai yang benerlah = '))
        if x <= 0 or y <= 0 or x > y:
            print('Batu lu kalau dibilangin')
        else:
            for i in range(y):
                if (i + 1) % x == 0:
                    print(i + 1, end = '\n')
                else:
                    print(i + 1, end = ' ')         
except:
    x = int(input('Masukkan nilai yang benerlah, awas salah lagi = '))
    y = int(input('Masukkan nilai yang benerlah, awas salah lagi = '))
    
    if x <= 0 or y <= 0 or  x > y:
        print('Batu lu kalau dibilangin')
    else:
        for i in range(y):
            if (i + 1) % x == 0:
                print(i + 1, end = '\n')
            else:
                print(i + 1, end = ' ')