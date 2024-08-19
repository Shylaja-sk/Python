#List is array
#my_shopping = ['milk','bread','apple']
#print(my_shopping)

name='Shylaja'
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))

#this is not possible - we cannot add string with interger
name="abc"
name = name+1
print(name)

#this is possible - after converting to str
name="abc"
name = name + str(1)
print(name)