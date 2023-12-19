# task 1\ 1)
sequence = [4, 8, 15, 16, 23, 42]

output = ' '.join(str(num) for num in sequence)
print(output)
#2
for i in sequence:
    print(i)

#3
rows = 7

for i in range(1, rows + 1):
    print('*' * i)
# 4 no need to do wtf is that

# 5) sum
first=int(input())
sec=int(input())
th=int(input())
print(first+sec+th)
# 6) volume of cube
edge_length = float(input("Enter the edge length of the cube: "))

volume = edge_length ** 3
surface_area = 6 * edge_length ** 2

print("Volume =", volume)
print("Surface Area =", surface_area)
#7)
num= int(input())
prev = num -1
next = num+1
print("previous: ", prev, ",next: ", next )

#8) same as a 5th problem

#9
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {difference_result}")
print(f"{num1} * {num2} = {product_result}")
#10)
centimeters = int(input("Enter the number of centimeters: "))

meters = centimeters // 100

print("Number of meters =", meters)

#TASK 2 1)
pass1= input()
pass2= input()
if pass1 == pass2:
    print("password accepted")
else : print("wrong shit")
#2)
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#3)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 < num2:
    smallest = num1
else:
    smallest = num2

print("Smallest number:", smallest)
#4)
age = int(input("Enter your age: "))

if age <= 13:
    age_group = "childhood"
elif age <= 24:
    age_group = "youth"
elif age <= 59:
    age_group = "maturity"
else:
    age_group = "old age"

print("Age group:", age_group)

#5)
side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))

if side1 == side2 == side3:
    triangle_type = "Equilateral"
elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle_type = "Isosceles"
else:
    triangle_type = "Versatile"

print("Triangle type:", triangle_type)
#TASK 3 )
n = int(input("Enter the height of the star rectangle (1-20): "))

star_line = "*" * 19

for _ in range(n):
    print(star_line)
# 2)
text = input("Enter a line of text: ")

for i in range(10):
    print(i, text)

# 3)
n = int(input("Enter the leg length of the right isosceles triangle (n >= 2): "))

for i in range(n, 0, -1):
    print("*" * i)
# sequence1
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

for num in range(m, n+1):
    print(num)
# sequence 2
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

if m < n:
    for num in range(m, n+1):
        print(num)
else:
    for num in range(m, n-1, -1):
        print(num)
# sequence 3
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

for num in range(m, n-1, -1):
    if num % 2 != 0:
        print(num)

#