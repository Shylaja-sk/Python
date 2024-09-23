#List mutable in nature  - it can change
squares = [1,4,9, 16,25]
squares[1]=26
print(squares)

#TUPLE -- less memory in tutple compared to list - duplicate is allowed in both
#Tuple is collection of Items

my_tuple = (1,4,9,16,25)
print(my_tuple)
# my_tuple[1]=30 Immutable in nature


#when there is chamges we will go with list and if no changes we will go with Tuple
shopping_list = ["bread","butter","jam","chips"]
shopping_list[3] = 'milk'
print(shopping_list)


#list has dynamic data
#tuple data is fixed so memory used less


a = (1,2,3,4,5)
b = (6,7.4,3,2,)
c = (a,b)
print(c)
print(c[0],[0])
print(c[1],[1])






