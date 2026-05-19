from array import *

# Creating a Homogenous array
val = array('i', [1,2,3,4,5,6])

# Printing all elements of an array
for x in val:
    print(x,end=" ")

print()

# Type code of array elements
print(val.typecode)

# Reversing an array
val.reverse()

for x in val:
    print(x,end=" ")

print()
# Insertion and update
val.insert(2,34) # insert at index 2

val.append(55) # insert at end

val[1] = 21 # Replace and override

for x in val:
    print(x, end=" ")

print()

# Copy array

arr = array(val.typecode, [x+1 for x in val])

for x in arr:
    print(x, end=" ")

print()

# Deleting 

val.pop(3) # delete array element at index 3

val.pop() # delete last element of array

val.remove(34) # remove element '34'

for x in val:
    print(x, end=" ")

print()

# slicing --> important 

# slicing --> reverse

arr2 = val[::-1]

for x in arr2:
    print(x, end=" ")

print()

# user input array

n = int(input("Enter size : "))
arr3 = array('i', [])
for i in range(n):
    x = int(input(f"Enter element {i}: "))
    arr3.append(x)

for x in arr3:
    print(x, end=" ")

print()

# Searching

ind = val.index(2)

print(ind)