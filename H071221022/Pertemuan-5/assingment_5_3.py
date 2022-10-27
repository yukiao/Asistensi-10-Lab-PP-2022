try : 
    array01 = set(map(int,input("Input array ke 1:" ).split()))
    array02 = set(map(int,input("Input array ke 2:" ).split()))
    duplikat = array01.intersection(array02)
    akhir = tuple(duplikat)
    print (f"Terdapat {len(duplikat)} buah duplikat yaitu {akhir} ")
except : 
    print ("input tidak valid")