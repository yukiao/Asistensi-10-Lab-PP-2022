class Kubus:
    def __init__(self, lebar, tinggi, panjang):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
    
    def setLebar(self, lebar):
        self.lebar = float(lebar)
    def setTinggi(self, tinggi):
        self.tinggi = float(tinggi)
    def setPanjang(self, panjang):
        self.panjang = float(panjang)
    def setMassa(self, massa):
        self.massa = float(massa)
    def getMassaJenis(self):
        return self.massa/(self.lebar*self.tinggi*self.panjang) 

lebar = float(input('masukkan lebar: '))
tinggi = float(input('masukkan tinggi: '))
panjang = float(input('masukkan panjang: '))
massa = float(input('masukkan masssa: '))

objKubus = Kubus(lebar, tinggi, panjang)

objKubus.setMassa(massa)
print("massa jenis = ", objKubus.getMassaJenis())
objKubus.setMassa(massa*2)
print("massa jenis = ", objKubus.getMassaJenis())