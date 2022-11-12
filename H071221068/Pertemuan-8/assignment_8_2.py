class Kubus():
    def __init__(self, lebar_k, tinggi_k, panjang_k):
        self.lebar = float(lebar_k)
        self.tinggi = float(tinggi_k)
        self.panjang = float(panjang_k)

    def setLebar(self, lebar_k):
        self.lebar = float(lebar_k)

    def setTinggi(self, tinggi_k):
        self.tinggi = float(tinggi_k)

    def setPanjang(self, panjang_k):
        self.panjang = float(panjang_k)

    def setMassa(self, massa_k):
        self.massa = float(massa_k)

    def volume(self):
        volume = self.panjang * self.lebar * self.tinggi
        return volume

    def getMassaJenis(self):
        massa_jenis = self.massa / self.volume()
        return massa_jenis

lebar = float(input('Lebar = '))
tinggi = float(input('Tinggi = '))
panjang = float(input('Panjang = '))
massa = float(input('Massa = '))

kubus = Kubus(lebar, tinggi, panjang)

print()
kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())

kubus.setMassa(massa*2)
print("Massa Jenis =", kubus.getMassaJenis())