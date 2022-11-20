class Person:
    def __init__(self, nama, umur, jenis_kelamin):
        self.name = nama
        self.age = int(umur)
        self.IsMale = bool(jenis_kelamin)

    def setNama(self, nama):
        self.name = nama
    
    def setUmur(self, umur):
        self.age = int(umur)
    
    def setJenisKelamin(self, jenis_kelamin):
        if jenis_kelamin == 'Male':
            self.IsMale = True
        else:
            self.IsMale = False

    def getNama(self):
        print(self.name)
    
    def getUmur(self):
        print(self.age)
        if self.IsMale == True:
            self.jenis_kelamin = 'Male' 
            print(self.jenis_kelamin)
        else:
            self.jenis_kelamin = 'Female'
            print(self.jenis_kelamin)

try:
    name = input('Name  : ')
    age = int(input('Age    : '))
    gender = input('Are you Male? (Yes or No)   : ')
    if gender == 'Yes':
        gender = bool(True)
    else:
        gender = bool(False)

    orang1 = Person(name, age, gender)
    print()
    orang1.getNama()
    orang1.getUmur()
except:
    print('Inputan tidak valid')