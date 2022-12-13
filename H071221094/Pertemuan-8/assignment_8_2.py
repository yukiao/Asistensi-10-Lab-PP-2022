



class Cube:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = float(panjang)
        self.lebar = float(lebar)
        self.tinggi = float(tinggi)

    def setPanjang(self, panjang):
        self.panjang = float(panjang)

    def setLebar(self, lebar):
        self.lebar = float(lebar)

    def setTinggi(self, tinggi):
        self.tinggi = float(tinggi)

    def setMassa(self, massa):
        self.massa = float(massa)

    def volume(self):
        volume = self.panjang * self.lebar * self.tinggi
        return volume

    def getMassaJenis(self):
        massa_jenis = self.massa / self.volume()
        return massa_jenis

try:
    panjang = float(input('Masukkan nilai panjang = '))
    lebar = float(input('Masukkan nilai lebar = '))
    tinggi = float(input('Masukkan nilai tinggi = '))
    massa = float(input('Masukkan nilai massa = '))

    kubus = Cube(panjang, lebar, tinggi)
    print()

    kubus.setMassa(massa)
    print(f"Massa jenis = {kubus.getMassaJenis()} Kg/m^3")

    kubus.setMassa(massa * 2)
    print(f"Massa jenis (jika nilai massa dikali 2) = {kubus.getMassaJenis()} Kg/m^3")
except:
    print('Inputan tidak valid')