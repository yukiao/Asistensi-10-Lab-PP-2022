def pemakaian (gol,daya,use):
        if gol == "R1" and daya >= 900 and daya < 1300 : 
            if daya == 900:
                x = use * 1352
            elif daya == 1300 : 
                x =  use * 1444.70
            elif daya == 2200 : 
                x = use * 1444.70
        elif gol == "R2" and daya >= 3.500 and daya < 5.500 :
            x = use * 1699.53
        elif gol == "R3" and daya >= 6.600 :
            x = use * 1699.53
        elif gol == "B2" and daya >= 6.600 and daya <= 200000 : 
            x = use * 1444.70
        elif gol == "B3" and daya >= 200000 : 
            x = use * 1114.74 
        elif gol == "I3" and daya >= 200000 : 
            x = use * 1314.12
        elif gol == "P1" and daya >= 6.600 and daya <= 200000 :
            x = use * 1523.28
        return ((x))
try :
    gol = input ("Golongan : ")
    daya = float(input ("daya : "))
    use = float(input ("pemakaian : "))
    using = pemakaian (gol,daya,use)
    a =  F"{using:_}"
    a1 = a.replace(".", ",")
    a2 = a1.replace("_", ".")
    print (F"jumlah tagihan anda:  {a2}")
except : 
    print ("Input Tidak Valid")
    


