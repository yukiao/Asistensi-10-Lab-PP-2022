def pekalian_2_matriks (matriks_pertama, matriks_kedua):
    x = [[1,2],[1,2]]
    for i in  range (len(matriks_pertama)) : 
        for a in range (len(matriks_kedua)) : 
            if i == 0 : 
                x[i][a]=(matriks_pertama[i][i]*matriks_kedua[i][a]) + (matriks_pertama[i][i + 1]*matriks_kedua[i+1][a])
            elif i == 1 : 
                x[i][a]=(matriks_pertama[i][i-1]*matriks_kedua[i-1][a]) + (matriks_pertama[i][i]*matriks_kedua[i][a])
    return x    
def input_matriks (matriks_pertama, matriks = "pertama"):
    x = 0
    for i in  matriks_pertama : 
        for a in range (len(i)) : 
            matriks_pertama[x][a]=int(input(f"Input nilai matriks {matriks} index {x+1},{a+1}:"))
        x = x + 1
try : 
    matriks_pertama = [[0,1],[0,1]]
    matriks_kedua = [[0,1],[0,1]]
    input_matriks (matriks_pertama, matriks = "pertama")
    input_matriks (matriks_kedua, matriks = "kedua")
    y = pekalian_2_matriks (matriks_pertama, matriks_kedua) 
    print ("Hasil perkalian matriks ")
    for i in range (len(y)) :
        for a in range (0,1) : 
            if i == 0 : 
                x = "x"
                sama = "="
            if i > 0 : 
                x = " "
                sama = " "
        print (f"| {matriks_pertama[i][a]}, {matriks_pertama[i][a + 1]} | {x} | {matriks_kedua[i][a]}, {matriks_kedua[i][a + 1]} | {sama} | {y[i][a]}, {y[i][a + 1]} | ")
except : 
    print ("input tidak valid")