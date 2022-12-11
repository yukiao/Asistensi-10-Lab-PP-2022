class Person:

    def __init__(self,name,age,isMale):
        self.name = name
        self.age = age
        self.isMale = isMale

    def setAge(self,age):
        self.age = age
    def getAge(self):
        return self.age
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def getgender(self):
        if self.isMale=="True":
            return "laki-laki"
        else:
            return "perempuan"        


name = input("Masukkan Name : ")
age = int(input("Masukkan Age : "))
ismale =(input("Masukkan isMale : "))  

Nur = Person(name, age, ismale)

print(Nur.getName())
print(Nur.getAge())
print(Nur.getgender())




   
        
    