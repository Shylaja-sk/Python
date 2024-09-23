#LIST - collection of items (duplicated are allowed

my_list = [1,"shy",3, True] #we can have diff data type
print(my_list)
print(len(my_list)) #len starts from one
print(my_list[1]) #index starts from 0
my_list[3] = "Sam"
#my_list[10] = "AA" not possible
print(my_list)

#indexing
print("Element at the index " ,my_list[3])

for element in my_list: # range is not required here
    print(element)


#Append new element AT THE END - and it cannot take multiple items - one by one only
my_list.append("shra")
my_list.append(50)
my_list.append(True)
print(my_list)

#Extend [] is required to add
my_list.extend([10,20,30,False])
print(my_list)

#Insert - it will shift the value when we insert before the
my_list.insert(0,"Amma")
print(my_list)
my_list.insert(-1,"lucky")

#To Replce
my_list[1] = "ABC"
print(my_list)
print("-------------------------------------")
#To remove
my_list.remove(30)
print(my_list)

#To make a copy
copy = my_list.copy()
my_list.clear()
print(my_list)
print(copy)

# copy.sort() - possible only when int is present
# copy.sort(reverse=false) - possible only when int is present

copy.reverse()
print(copy)
















