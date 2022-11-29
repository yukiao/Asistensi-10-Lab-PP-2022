from Hero import Warrior, Assassin, Support
warrior = Warrior("bambang",  posistion = 10)
warrior = Warrior("bambang",  posistion= 10)
assassin = Assassin("joko",  posistion = 25)
support = Support("udin", posistion = 30)
# sebelum
print("health (before)", warrior.gethealth())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.gethealth())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.gethealth())
print("Support (speed) : ",support.getspeed())
support.spesial(warrior)
# sesudah
print("Warrior (health)", warrior.gethealth())
print("Support (speed): ",support.getspeed())
