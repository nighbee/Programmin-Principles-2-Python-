#ising as in cpp, no difference
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) #tru list
#also can be used tru words str
for x in "banana":
  print(x)
# also can be added conditions in For
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#can be used in range
for x in range(10):
    print(x) #cout nums from [0,10)
#also can define start pos and pos and parametr of steps
for i in range(2, 30 , 3): # this "3" is step to next num
    print(i)
#nested loops, like in cpp mothing special
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#if for loop have no content write pass
for x in [0, 1, 2]:
  pass
#exercise
fruits=["apple", "banana", "cherry"]
for i in fruits:
    print(i)