#Set
#Set is a collection of unique element
# {}


a = {"a","b","c","a"} # it removed suduplicates
print(a)

list1 = [1,2,4,4,4,5,5,5,5,6,7,7,7,7]
set1 = set(list1) #convered to list
print(set1)

# Set with Union
set11 = {1,2,3,4}
set2 = {4,6,7,8}
set3 = set11.union(set2)
print(set3)

set11 = {1,2,3,4}
set2 = {4,6,7,8}
set3 = set11.intersection(set2)
print(set3)

set11 = {1,2,3,4}
set2 = {4,6,7,8}
set3 = set11.difference(set2)
print(set3)

set11 = {1,2,3,4}
set2 = {4,6,7,8}
set3 = set2.difference(set11)
print(set3)

set11 = {1,2,3,4}
set2 = {4,6,7,8}
set3 = set2.issubset(set11)
print(set3)
