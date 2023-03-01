from functools import reduce
from time import sleep
import math, time
#1 multiplie all nums in list
list=[range(1,11)]
r1=reduce((lambda x,y: x*y), list)
print(r1)
#2 string and calculate the number of upper case letters and lower case letters
str1='AlmazToktasin KBTU pp courSe'
def nums_of_occur(s):
    small_case=0
    upper_case=0
    for letter in s:
        if letter.isupper():
            upper_case+=1
        elif letter.islower():
            small_case+=1
    return upper_case, small_case
x,y=nums_of_occur(str1)
print(x,y)
#3 palindrome of shit
str2='abba'
def pal_or_not(s):
    s1=s[::1]
    if s1==s:
        return 'palindrome'
    else:
        return 'shit no'
r3=pal_or_not(str2)
print(r3)
#4 function of root after some time
# Define the function to compute the square root after a specified number of milliseconds
def sqrt_after_delay(number, delay):
    # Wait for the specified number of milliseconds
    time.sleep(delay / 1000)

    # Compute the square root of the number
    result = math.sqrt(number)

    # Return the result
    return result


# Test inputs
number = 25100
delay = 2123

# Compute the square root after the specified delay
result = sqrt_after_delay(number, delay)

# Print the result
print(f"Square root of {number} after {delay} milliseconds is {result}.")
#5




