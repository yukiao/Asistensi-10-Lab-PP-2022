class Person:
    def __init__(self, nama, umur, laki_laki):
        self.nama = nama                            # klo ada ini gausa pake set()
        self.umur = umur
        self.laki_laki = laki_laki
    
    def getAge (self):
        print(f"umur: {self.umur} Tahun")
    
    def getName (self):
        print (f"nama: {self.nama}")
    
    def getGender (self):
        if self.laki_laki == 'laki-laki':
            self.laki_laki = True
            if self.laki_laki == True:
                print("True")
        elif self.laki_laki == 'perempuan':
            self.laki_laki = False
            if self.laki_laki == False:
                print ("False") 
        else: 
            print("inputan salah")

name = input("masukkan nama: ")
age = int(input("masukkan umur: "))
isMale = input("masukkan gender: ")

human = Person(name, age, isMale)           #objek

human.getName()
human.getAge()
human.getGender()