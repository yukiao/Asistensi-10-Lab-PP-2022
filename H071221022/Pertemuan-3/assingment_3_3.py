try :
    x = int (input())
    y = int (input())
    if x < y : 
        kembalian = y - x 
        Rp100 = kembalian //100000
        Rp50  = (kembalian-((Rp100)*100000))//50000
        Rp20  = (kembalian-(((Rp100)*100000)-(Rp50)*50000))//20000
        Rp10  = (kembalian-(((Rp100)*100000)-(Rp50)*50000)-(Rp20)*20000)//10000
        Rp5   = (kembalian-(((Rp100)*100000)-(Rp50)*50000)-(Rp20)*20000-(Rp10)*10000)//5000
        Rp2   = (kembalian-(((Rp100)*100000)-(Rp50)*50000)-(Rp20)*20000-(Rp10)*10000-(Rp5)*5000)//2000
        Rp1   = (kembalian-(((Rp100)*100000)-(Rp50)*50000)-(Rp20)*20000-(Rp10)*10000-(Rp5)*5000-(Rp2)*2000)//1000
        print (f"{Rp100} uang Rp. 100.000")
        print (f"{Rp50} uang Rp. 50.000")
        print (f"{Rp20} uang Rp. 20.000")
        print (f"{Rp10} uang Rp. 10.000")
        print (f"{Rp5} uang Rp. 5.000")
        print (f"{Rp2} uang Rp. 2.000")
        print (f"{Rp1} uang Rp. 1.000")
    elif  x > y : 
        print ("Uang anda kurang")
    elif x == y : 
        print ("uang anda pas")
except : 
    print (("Input haris angka "))