class Human : 
    def __init__(self,name, pos_x ):
        self.name = name 
        self.__pos_x = pos_x
    
    def movement(self,arah, speed):
        if arah == "L":
           self.__pos_x = self.__pos_x - speed
        elif arah == "R":
            self.__pos_x = self.__pos_x + speed
    def getname(self):
        return (self.name)
    def setname(self, x):
        self.name = x
        
    def getposistion(self):
        return (self.__pos_x)
    def setposistion(self, x):
        self. __pos_x = x
        
class Hero(Human) :
    def __init__(self,name,posistion):
        super().__init__(name, posistion)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    def getpower (self):
        return (self._power)
    def setpower(self, x):
        self._power = x
       
    def gethealth(self):
        return (self._health)
    def sethealth(self, x):
        self. _health = x
       
    def getarmor(self):
        return (self._armor)
    def setarmor(self, x):
        self. _armor = x
        
    def getspeed (self):
        return (self._speed )
    def setspeed (self, x):
        self. _speed  = x
       
    def attack (self, target):
        target._health = target._health - self._power
class Warrior(Hero):
    def __init__(self,name,posistion):
        super().__init__(name, posistion)
        self._power = 26
        self._armor = 30
    def spesial (self, target):
        self._armor = 45 
        self._power = 32
        target.sethealth(target.gethealth()-32) 
class Assassin(Hero):
    def __init__(self,name,posistion):
        super().__init__(name, posistion)
        self._power = 35
        self.speed = 4
    def spesial (self, target):
        self._power = 42 
        self.speed = 7
        target.sethealth(target.gethealth()-42) 
class Support(Hero):
    def __init__(self,name,posistion):
        super().__init__(name, posistion)
        self._power = 35
        self.speed = 4
    def spesial (self, target):
        self._speed = 6
        target.sethealth(target.gethealth()+150) 


        
    

    

    
        



        
    





            



