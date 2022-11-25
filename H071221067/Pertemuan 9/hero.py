class Human:
    def __init__(self, name, position):
        self.name = name
        self.__pos_x = position
    
    def setArah(self, arah):
        if arah == 'L':
            self.__pos_x -= self._speed
        elif arah == 'R':
            self.__pos_x += self._speed

class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        target.setHealth(target.getHealth() - self._power)

    def setHealth(self, health):
        self._health = health

    def getHealth(self):
        return self._health

    def getSpeed(self):
        return self._speed

class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30
    
    def special(self, target):
        self._armor = 45
        self._power = 32
        target.setHealth(target.getHealth() - self._power)

class Assassin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power  = 35
        self.speed = 4

    def setSpeed(self):
        self.speed = 4

    def getSpeed(self):
        return self.speed

    def special(self, target):
        self.speed = 7
        self._power = 42
        target.setHealth(target.getHealth() - self._power)

class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self.speed = 4
    
    def setSpeed(self):
        self.speed = 4

    def getSpeed(self):
        return self.speed

    def special(self, target):
        self.speed = 6
        target.setHealth(target.getHealth() + 150)