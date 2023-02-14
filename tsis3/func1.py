# 1st problem
def func(gr):
    return 28.349*gr
gr = int(input())
ou= func(gr)
print(ou)

#2nd problem
def FahToCen(fah):
    return ((5/9)*(fah-32))
fah = int(input())
cen=FahToCen(fah)
print(cen)

#3rd problem
def solve(numhead, numleg):
    for i in range(numhead+1):
        j=numhead-1
        if 2*i+4*j == numleg:
            return i,j
    return (None, None)
numleg=94
numhead=35
chicken, rabbit= solve(numhead,numleg)
if chicken== None:
    print('No solution')
else:
    print("Num of chickens: ", chicken)
    print("Num of rabbits: ", rabbit)

# 4 th prob

# def filt(nums):
#     def isPrime(num):
#         if num<2:
#             return False
#         else:
#             for i in range(2, int(nums**0.5)+1):
#                 if num%i==0:
#                     return False
#         return True
#     return [num for num in nums if isPrime(num)]
#
# nums=map(int, input().split())
# print(filt(nums))


# 5

# 6TH PROB
def rev(sent):
    word= sent.split()
    return ' '.join(reversed(word))
sent=input()
print(rev(sent))

# 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums = [int(x) for x in input("Enter a list of integers, separated by spaces: ").split()]
print(has_33(nums))

# 8
def has_007(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i+2]==7:
            return True
    return False

nums = [int(x) for x in input("Enter a list of integers, separated by spaces: ").split()]
print(has_007(nums))

# 9
def volSph(r):
    return (4/3*3.14*r*r)
r= int(input())
vol=volSph(r)
print(vol)

# 10
def unique(nums):
    uni_el=[]
    for elem in nums:
        if elem not in uni_el:
            uni_el.append(elem)
    return uni_el

nums=[int(x) for x in input("Enter a list of integers, separated by spaces: ").split()]
print(unique(nums))

# 11
def palin(st):
    if st == st[::-1]:
        return True
    else:
        return False
st= input()
print(palin(st))

# 12
def histo(nums):
    for i in nums:
        print('*'*i)
nums=[int(x) for x in input("Enter a list of integers, separated by spaces: ").split()]
print(histo(nums))

