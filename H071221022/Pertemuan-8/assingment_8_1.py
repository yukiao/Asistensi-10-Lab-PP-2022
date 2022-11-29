class Person : 
    def __init__(self, nama, umur, male):
        self.__name = nama
        self.__age = umur
        self.__IsMale = male

    def getage (self):
        return(self.__age)
    def setage (self, x):
        self.__age = x
        return self.__age
    def setname(self,x) :
        self.__name = x
        return self.__name
    def setGendre(self, x) :
        if x == "Female" :
            x = False
        else :
            x = True
        self.__IsMale = x
        return(self.__IsMale)
    def getGendre (self):
        if self.__IsMale :
            return("Male")
        else : 
            return("Female")  
nama = input ()
umur = int(input())
male = True 
beny = Person(nama,umur, male )
beny.setage(umur)
print (beny.getage())