import math
h = float(input())
a = float(input())
b = float(input())

x_dan_y = h * (math.tan(math.radians(a)))
y = h * (math.tan(math.radians(b)))
x = x_dan_y - y

print(round(x, 1), "m")