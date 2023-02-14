# array, like in cpp and like an lists same shit. Example:
cars=["ford", 'lada', 'volvo']
#u can acces by index like in cpp, index starts from 0
x=cars[0]
#modifying
cars[2]='Dee'
for i in cars:
    print(i)
print(len(cars))
# add element by "append" example
cars.append("Jiguli")
#removing by pop(position) or remove(name of component)
cars.pop(1)
cars.remove('Jiguli')
for i in cars:
    print(i)
print(len(cars))
"""
append()	Adds an element at the end of the list
clear()  	Removes all the elements from the list
copy()  	Returns a copy of the list
count() 	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position, insert(pos, var)
pop()	    Removes the element at the specified position, pop(pos)
remove()	Removes the first item with the specified value, remove(var)
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""