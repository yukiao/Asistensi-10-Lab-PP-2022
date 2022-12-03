from abc import ABC, abstractmethod
class Bangun(ABC) :
    @abstractmethod
    def keliling():
        pass
    def luas ():
        pass
    def volume ():
        pass
class Datar(Bangun):
    def __init__ (self, panjang):
        self.__panjang = panjang 
        self.__lebar = panjang
    def keliling(self):
        x = (self.__panjang + self.__lebar)*2
        return x
    def luas(self):
        x = (self.__lebar * self.__panjang)
        return x
    def volume(self):
        print ("Tidak memiliki volume")
class Persegi(Datar):
    def __init__(self, panjang, lebar):
        super().__init__(panjang)
        self.__panjang = panjang 
        self.__lebar = lebar
class Segitiga_sikusiku (Datar):
    def __init__(self,panjang, lebar ):
        super().__init__(panjang, lebar)
    def luas (self):
        x = 1/2*(self.__panjang*self.__lebar)
        return x
    def keliling (self):
        x = self.__panjang + self.__lebar + ((self.__panjang**2 + self.__lebar**2)**1/2)
        return (round(x , 2))
persegi = Persegi(12, 10)
print (persegi.luas())



    

    


        




