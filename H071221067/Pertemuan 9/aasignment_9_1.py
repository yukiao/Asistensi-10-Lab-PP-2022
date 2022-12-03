from hero import Warrior,Support,Assassin

warrior = Warrior("Orii", pos_x=10)
assassin = Assassin("Apip", pos_x=25)
support = Support("Ocang", pos_x=30)

#sebelum
print("health (before)", warrior.getHealth())

assassin.attack(warrior)

#sesudah
print("health (after)", warrior.getHealth())

print("-"*10)

#sebelum
print("warrior (health)", warrior.getHealth())
print("support (speed)", support.getSpeed())
support.special(warrior) 

#sesudah
print("warrior (health)", warrior.getHealth())
print("support (speed)", support.getSpeed())

