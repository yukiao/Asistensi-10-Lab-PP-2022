class AnggotaKampus:

   
    nama_institusi = "UNIVERSITAS XYZ"
    tambahan_gaji=250000
    #"representasi anggota kampus"
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        self.pendapatan_tambahan=0
        print('membuat anggota baru pada kampus: %s' % self.nama)

    def tambahan(self):
        self.pendapatan_tambahan += self.tambahan_gaji

    def info(self):
       # "info"
        print('Nama: %s, Umur: %s' % (self.nama, self.umur))

# subclass
class Dosen(AnggotaKampus):
   # "representasi guru"
    def __init__(self, nama, umur, gaji):
        AnggotaKampus.__init__(self, nama, umur)
        self.gaji = gaji
        print('membuat Dosen : %s' % self.nama)

    def info(self):
        AnggotaKampus.info(self)
        print('Gaji: %s' % self.gaji)

    
    def tambahan(self):
        #gaji tambahan pada class Dosen sebesar
        # 10% dari gajinya
          self.pendapatan_tambahan = self.gaji*0.1
          print('Tambahan Gaji: %s' % self.pendapatan_tambahan)


# subclass
class Mahasiswa(AnggotaKampus):
    "representasi Mahasiswa"
    def __init__(self, nama, umur, nilai):
        AnggotaKampus.__init__(self, nama, umur)
        self.nilai = nilai
        print('membuat mahasiswa: %s' % self.nama)

    def info(self):
        AnggotaKampus.info(self)
        print('Nilai: %s' % self.nilai)


namaDosen=input("Nama Dosen : ")
umurDosen=input("Umur Dosen : ")
gajiDosen=int(input("Gaji Dosen : "))

print()
namaMahasiswa=input("Nama Mahasiswa : ")
umurMahasiswa=input("Umur Mahasiswa : ")
nilaiMahasiswa=input("Nilai Mahasiswa : ")
print()

dosen = Dosen(namaDosen, umurDosen, gajiDosen)
mahasiswa = Mahasiswa(namaMahasiswa,umurMahasiswa, nilaiMahasiswa)

# cetak baris kosong
print()
anggota = [dosen, mahasiswa]

for orang in anggota:
    orang.info()
    orang.tambahan()