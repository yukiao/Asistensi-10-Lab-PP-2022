from assignment_9 import Warrior,Assassin,Support

warrior=Warrior("Fahri", pos_x=10)
assassin=Assassin("Zul", pos_x=25)
support=Support("Adnan", pos_x=30)

#GET HEALTH (Sebelum)
print("---Sebelum Impact---")
print("health (before) : ", warrior.getHealth())
assassin.attack(warrior)
#GET HEALTH (Sesudah)
print("---Setelah Impact---")
print("Health (After) : ", warrior.getHealth())

print("="*25)

#GET SPEED (Sebelum)
print("---Sebelum Impact---")
print("Support (Speed) : ", support.getSpeed())

support.special(assassin)

#GET HEALTH (Sesudah)
print("---Setelah Impact---")
print("Support (Speed) : ", support.getSpeed())


#GET POSISI
print("---Posisi Warrior")
print("Posisi Warrior :", warrior.getPosisi())

print("="*25)