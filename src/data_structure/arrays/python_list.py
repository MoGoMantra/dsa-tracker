# ordered , changeable(mutable) , allow duplicates , indexed
list_var = ["hey", 20, True, 20 , 45j, 23.678 ] #assignment with multiple data types and duplicates
print(list_var[2],list_var[-2],list_var[:3],list_var[1:],list_var[-5:-2],sep='-') #indexing
print(len(list_var)) # length
l = list("hello") #casting
print(l)
if 20 in list_var: #if item is in / not in the list
    print('True')
#Changing
list_var[2] =34.80  # change / replace values /range of values
print(list_var)
list_var[2:7]=[1,2,3,4,5] # length will also change
print(list_var,len(list_var))
#Adding
list_var.insert(1,"no") # will not replace just insert it
print(list_var,len(list_var))
list_var.append(666) #adding item (at the end)
print(list_var,len(list_var))
# Extend -> add /append elements from other iterable (list/tuple/sets/dict) to current
var_l = [ 0, 0.1 , 0.3]
list_var.extend(var_l)
print(list_var,len(list_var))
list_var.insert(5,20)
print(list_var,len(list_var))
# Removing 
list_var.remove(0.1) #specified item
print(list_var,len(list_var))
list_var.remove(20) #specified item-> multiple times-> remove first iteration
print(list_var,len(list_var))

list_var.pop(3)
print(list_var,len(list_var)) # remove the specified indexed item
list_var.pop()
print(list_var,len(list_var)) # remove the last item

del list_var[4]
print(list_var,len(list_var)) #delete the specified item
# del list_var
# delete the list throws an error, as list deleted no printing
# print(list_var,len(list_var)) 
list_var.clear()
print(list_var,len(list_var)) #clear all contained in the list

#looping

for x in list_var:
    print(x,end=" ")

print("\n")

for i in range(len(list_var)):
    print(list_var[i],end=" ")

print("\n")

i = 0 
while i<len(list_var):
    print(list_var[i],end=" ")
    i+=1

print("\n")
#list comprehension
a = [x*2 for x in list_var] # a is the new list, taking reference of list_var; 
print(type(a),a,len(a),sep="\n") # for looping
print("\n")
# newlist = [expression for item in iterable if condition == True]

b=[x for x in list_var]
c=[x for x in list_var if x!=20]
d=[type(x) for x in list_var]
e=[x for x in range(10) if x<=5]
f=["ok" for x in list_var] # expression can be something new, iterating threw list, 
g=[x if x!=20 else 2*x for x in list_var]
print(b,c,d,e,f,g,sep="\n")

# sorting

h = [1,5,3,7,12]
i = ["Abkjasd", "dsflkj", "dsflkjiweo", "ABHDSIFOI"]
# IMP --> print(var.method()) --> returns None
print(h.sort())
print(i.sort(reverse=True))
h.sort() #sorting in accending order
print(h)
h.sort(reverse=True) #sorting in descending order
print(h)
#CALLABLE --> an object that can be called, poss. with a set of arguments. like func,methods,..
# parameter "key" is used in built-in functions like sort(), min(), max(), to customize comparison
# key = {must be a callable} that takes single arguement (iterable) , eaach element of iterabale
# go through callable and return a key used in comparison.

i.sort(key=len)
print(i)
i.sort()
print(i) # case -sensitive sort --> capital first
def myfun(n):
    return abs(n-9/2)
h.sort(key=myfun)
print(h)
# case - insesitive sort
i.sort(key=str.lower)
print(i)
i.sort(reverse=True) #reverse the order in case of string but for int type its descending order
print(i) 
i.reverse() #also for reversing the order
print(i)

#copying
# list 2 =list 1 --> list 1 change will change list2 also, so no copying
j=list_var.copy()
k=list(list_var)
list_var.append("hey")
print(j)
print(k)
print(list_var)

l=list_var[:6]
m=list_var[:]
list_var.append("hey")
print(l)
print(m)
print(list_var)

#Joining the lists
n=list_var+var_l # join in third list
print(n)
#joining in same list
for x in var_l:
    list_var.append(x)
print(list_var)
list_var.extend(var_l)
print(list_var)

# list_var.append(item)
# list_var.clear()
# list2 = list1.copy() { copy() returns a list }
# list_var.count(0) { count() returns a number }
# list.extend(iterable) { add elements of iterable to list in end}
# list.index(element,start,end) --> list_var.index(0,4,20) --> returns the index of 0 in range 4-20 indexing
# list_var.insert(2,"value") --> insert "value" at index 2 --> and shift remaining in back --> adding not changing
# list_var.pop(pos) --> pop the pos indexed item , default -1 indexed i..e last item
# list_var.remove("element") --> removes the first occurence of the element
# list.reverse() --> reverse the order of the list
# list.sort(reverse=True|False , key=callable) -> sort accordingly

# Python Code --> reverse traversal
arr = [1, 2, 3, 4, 5]

print("Reverse Traversal: ", end="")
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")
print()