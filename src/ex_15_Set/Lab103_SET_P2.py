a = {1,2,3}
b =  {3,4,5}
print(a|b)       # {1, 2, 3, 4, 5}
print(a.union(b))                # same result

print(a & b)              # {3}
print(a.intersection(b))  #Intersection means common elements in both sets.

print(a-b)    #elements in a but NOT in b
print(b-a)    #elements in b but NOT in a

print(a ^ b) #Gives elements that are NOT common in both sets  {1, 2, 4, 5}

set1 = {1,2,3}
set2 = {4,5,6}
my_set = set1.union(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

my_set = set1.intersection(set2)
print(my_set)

my_set = set1.difference(set2)
print(my_set)

my_set = set2.difference(set1)
print(my_set)