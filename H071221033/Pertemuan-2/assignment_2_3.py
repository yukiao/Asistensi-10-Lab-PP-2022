# praktikum 2 no 3

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a > b and a > c:
    print(a, "adalah nilai terbesar")
elif b > c:
    print(b, "adalah nilai terbesar")
else:
    print(c, "adalah nilai terbesar")