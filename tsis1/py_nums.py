x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))



x1 = 1
y1 = 35656222554887711
z1 = -3255522

print(type(x1))
print(type(y1))
print(type(z1))

x2 = 1.10
y2 = 1.0
z2 = -35.59

print(type(x2))
print(type(y2))
print(type(z2))

x3 = 3+5j
y3= 5j
z3 = -5j

print(type(x3))
print(type(y3))
print(type(z3))


x4 = 1    # int
y4 = 2.8  # float
z4 = 1j   # complex

#convert from int to float:
a = float(x4)

#convert from float to int:
b = int(y4)

#convert from int to complex:
c = complex(x4)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1, 10))