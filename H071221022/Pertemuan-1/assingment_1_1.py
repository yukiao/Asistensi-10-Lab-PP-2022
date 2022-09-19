from math import pi, tan
h,a,b = 100,60,45
sudut01 = a*(pi/180)
sudut02 = b*(pi/180)
c = (tan(sudut01) - tan(sudut02))*h
print (f"{round(c, 1)} m")