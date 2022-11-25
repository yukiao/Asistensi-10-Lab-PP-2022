from assignment_9_Hero import Warrior,Assassin,Support

warrior=Warrior("Ardi", pos_x=10)
assassin=Assassin("Dani", pos_x=25)
support=Support("Aya", pos_x=30)

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