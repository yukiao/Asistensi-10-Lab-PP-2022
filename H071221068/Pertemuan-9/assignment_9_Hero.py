class Human:
    def __init__(self, nama, posisi):
        self.name = nama
        self.__pos_x = posisi
        self._speed = 1 

    def movement(self, arah):
        if arah == 'L':
            self.__pos_x -= self._speed
        elif arah == 'R':
            self.__pos_x += self._speed

    def getPosisi(self):
        return self.__pos_x

    def getSpeed(self) :
        return self._speed

    def setSpeed(self, newSpeed) :
        self._speed = newSpeed 

class Hero(Human):
    def __init__(self, nama, pos_x):
        super().__init__(nama, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        # target._health -= self._power
        newHealth = target.getHealth() - self._power
        target.setHealth(newHealth) 

    def getPower(self):
        return self._power
    
    def setPower(self, newPower) :
        self._power = newPower

    def getHealth(self):
        return self._health

    def setHealth(self, newHealth) :
        self._health = newHealth

    def getArmor(self):
        return self._armor

    def setArmor(self, newArmor) :
        self._armor = newArmor

    def getSpeed(self):
        return self._speed
    
    def setSpeed(self, newSpeed) :
        self._speed = newSpeed

class Warrior(Hero) :
    def __init__(self, nama, pos_x):
        super().__init__(nama, pos_x )
        self._power = 26
        self._armor = 30

    def special(self, target) :
        self._armor = 45
        self._power = 32
        self.attack(target)

class Assassin(Hero) :
    def __init__(self, nama, pos_x):
        super().__init__(nama, pos_x )
        self._power = 35
        self._speed = 4
    
    def special(self, target) :
        self._speed = 7
        self._power = 42
        self.attack(target)

class Support(Hero) :
    def __init__(self, nama, pos_x):
        super().__init__(nama, pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target) :
        self._speed = 6
        # target._health = target._health + 150
        newHealth = target.getHealth() + 150
        target.setHealth(newHealth) 