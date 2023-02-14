#1
n=int(input())
a= [i**2 for i in range(1,n+1)]
print(a)
#2
even=[i for i in range(1,n+1) if i%2==0]
print(even)
#3
def generate_shit(n):
    return (num for num in range(n+1) if num%3==0 and num%4==0)
print(generate_shit(n))
#4
a=int(input())
b=int(input())
def squares(a,b ):
    num= a
    while num<b:
        yield num*num
        num+=1
for num in squares(a,b):
    print(num)
#5
def shit(n):
    shit=n
    while shit!=0:
        yield shit
        shit -=1
for shit in shit(n):
    print(shit)
