list1 = [2, 5, 3, 8, 1 , 1, 9, 4]

print(list1)

list1.append(6)
print(list1)

list1.pop(2)
print(list1)

list1.insert(0, 45)
print(list1)

list1.remove(1)
print(list1)

list2 = sorted(list1)
print("list2: ",list2)
print("list1: ",list1)
list1.sort()
print(list1)

print()

L = [23, "Obama", 34.5, "taco", "45", "HI"]

for elem in L:
    i = 0
    print("Element #","i: ",elem)
    i = i +1

# Range

list_range = []
for i in range (0, 100, 5): # This doesn't include 100.
    list_range.append(i)

print(list_range)
print(f"Max in list_range: {max(list_range)}")
print(f"Min in list_range: {min(list_range)}")
print(f"Sum in list_range: {sum(list_range)}")

# Or we can write range(#Just the number we go up to) 
# In here increment will be 1++ and starting number will be 0

for i in range(5):
    print(i)

# Slicing a list <list> [start:stop]

slicing_list = list_range[3:6]
print(f"Slicing list_range from 3 to 6: {slicing_list}")

# SHALLOW COPY

# This creates what it is called "Shallow Copy". 
# There is only one list made in this code.
# But  this is refering two ways.
# So, changing from one refering will cause changing the list.
# This shallow copy happens in only lists.

# The solution for this....
# BY CREATING A DEEP COPY (LIKE SLICYING THE LIST BUT FULL RANGE)
# lis1 = [1, 2, 3]
# list2 = list1[:]

#TUPLES

# This is just a list that cannot be changed.
# In other words tuples are immutable
# my_pets = ("Dog", "cat")

range1 = range(0,10,1)
print(list(range1))
print([*range1])


list3 = [4, 6, 7, 8]

print(list3)

for elem in list3:
    elem = elem*2

print(list3)








