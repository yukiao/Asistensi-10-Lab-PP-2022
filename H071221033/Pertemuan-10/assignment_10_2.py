
class Buku:
    def __init__(self, judul, penulis):
        self._judul = judul
        self._penulis = penulis

    def getJudul(self):
        return self._judul

    def setJudul(self, judul):
        self._judul = judul
        
    def getPenulis(self):
        return self._penulis

    def setpenulisl(self, penulis):
        self._penulisl = penulis

    def membandingkan(self):
        pass

class Novel(Buku):
    def __init__(self, judul, penulis):
        super().__init__(judul, penulis)

    def membandingkan(self, target):
        print("Membaca novel sangat menyenangkan daripada " + target.getJudul()+ "!")

class Artikel(Buku):
    def __init__(self, judul, penulis):
        super().__init__(judul, penulis)

    def membandingkan(self, target):
        print("Isi artikel sulit dimengerti dibanding " + target.getJudul())

a = Novel("Novel", 'abc')
b = Artikel("Artikel", 'Dilah')

b.membandingkan(a)
a.membandingkan(b)





#class abstrak
from abc import ABC, abstractmethod
 
class Kendaraan(ABC):
    @abstractmethod
    def muatan(self):
        pass
 
class Mobil(Kendaraan):
    def muatan(self):
        print("menampung 6 penumpang")
 
class Motor(Kendaraan):
    def muatan(self):
        print("menampung 2 penumpang")
r = Mobil()
r.muatan()

p = Motor()
p.muatan()
