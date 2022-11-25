from math import pi

class Bentuk:
    def __init__(self, name):
        self.name = name

    def luas(self):
        pass

    def ciri(self):
        return "Bangun datar dua dimensi"

    def __str__(self):
        return self.name


class Persegi(Bentuk):
    def __init__(self, panjang):
        super().__init__("Persegi")
        self.panjang = panjang

    def luas(self):
        return self.panjang**2

    def ciri(self):
        return "Memiliki empat sudut"


class Lingkaran(Bentuk):
    def __init__(self, radius):
        super().__init__("Lingkaran")
        self.radius = radius

    def luas(self):
        return pi*self.radius**2

class Segitiga(Bentuk):
    def __init__(self, alas, tinggi):
        super().__init__("Segitiga")
        self.alas = alas
        self.tinggi = tinggi
    
    def luas(self):
        return (self.alas * self.tinggi)/2

    def ciri(self):
        return "Memiliki tiga sudut"


a = Persegi(4)
b = Lingkaran(7)
c = Segitiga(3,4)

print(a)
print(b)
print(c)

print(10*"=")

print(a.ciri())
print(b.ciri())
print(c.ciri())

print(10*"=")

print(a.luas())
print(b.luas())
print(int(c.luas()))