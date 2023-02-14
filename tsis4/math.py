import math
#1
deg=int(input())
print(math.radians(deg))
#2
h=5
b1=5
b2=6
print("Area ",(b1+b2)/2*h)
#3
n = 4
s = 25
area = (s ** 2 * n) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", area)
#4
b=int(input())
h_p=int(input())
print(h_p*b)
