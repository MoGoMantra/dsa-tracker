from numpy import *

# Heterogenous array

a1 = array((1,2,3.4,6,True))

for x in a1:
    print(x, end=" ")

print()

# Changing the type of elements
a2 = array((1.4,2.6,3.8),int)

for x in a2:
    print(x, end=" ")

print()

a3 = linspace(10,20,4) # 10,20 included in 4 partitions

for x in a3:
    print(x, end=" ")

print()

a4 = arange(10,20,2) # 20 not inc, 2-> no. of steps

for x in a4:
    print(x, end=" ")

print()

a5 = logspace(10,20,10) # 10 - no. of elements between 10^10 and 10^20 equally dist.

for x in a5:
    print(x, end=" ")

print()

a6 = zeros(10)

for x in a6:
    print(x, end=" ")

print()

a7 = ones(10)

for x in a7:
    print(x, end=" ")

print()

a8 = full(10,3) # size 10 , value 3

for x in a8:
    print(x, end=" ")

print()

# Multidimensional array --> dimensions should be homogeneous

zero = array(10) # 0-d

print(zero)

#1-d
one = array((1,2,3))
for x in one:
    print(x, end=" ")

print()

#2-d
two = array(((1,2),(3,4)))
for x in two:
    print(x)

# 3-d

three = array((((1,2),(3,4)),((5,6),(7,8))))

for x in three:
    for y in x:
        print(y,end=" ")
    print()

print()

