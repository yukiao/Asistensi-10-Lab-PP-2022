class Person:

    def __init__(self , name , age , isMale):
        self.name = name
        self.age = age
        self.isMale = isMale
    def setAge(self , age):
        self.age = age
    def setName(self , name):
        self.name = name
    def setGender(self , isMale):
        self.isMale = isMale
    def getAge(self):
        return self.age
    def getName(self):
        return self.name
    def getGender(self):
        return self.isMale

name = input('name: ')
age = int(input('age: '))
isMale = input('Male? (yes or no): ')
if isMale == 'yes':
    isMale = True
else:
    isMale = False

person = Person(name , age , isMale)

print(person.getName())
print(person.getAge())
print(person.getGender())