from abc import ABC,abstractmethod

class mahluk_hidup(ABC):
    @abstractmethod
    def gerak():
        pass

class Hewan(mahluk_hidup):
    def __init__(self,nama):
        self.nama = nama
    def gerak(self):
        print('gerak-gerak!!!')
class HewanDarat(Hewan):
    def __init__(self,nama,kaki=0):
        super().__init__(nama)     # Inheritence
        self.__kaki = kaki         
        
    def gerak(self):             # Polymorphism
        print(self.nama,'gerak di darat dengan kaki',self.__kaki)

class HewanAir(Hewan):
    def __init__(self,nama,sirip='kecil'):
        super().__init__(nama)     # Inheritence
        self.__sirip = sirip      
        
    def gerak(self):             # Polymorphism
        print(self.nama,'gerak di air dengan sirip', self.__sirip)


hewan = Hewan('pokoknya hewan')
kambing = HewanDarat('kambing',kaki=4)
hiu = HewanAir('hiu',sirip='lebar')

hewan.gerak()
kambing.gerak()
hiu.gerak()        