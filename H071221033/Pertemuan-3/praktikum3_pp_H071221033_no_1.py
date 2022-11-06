try:
    x = int(input( ))
    y = int(input( ))
    if x < y:
        for i in range(1, y+1):             # y+1 biar output y = input y
            print(i, end=' ')               # end= ' ' biar outputnya menyamping bkn kebawah
            if i%x==0 :
                print()
    else:
        print('Error')
except:
    print("Inputan tidak sesuai")
