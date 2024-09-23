#Serach in Tuple

city = ("Bangalore","Hydrabad","Chennai","Delhi")
print("Bangalore" in city)
print("New delhi" in city)

#Tuples cannot  be appended - to do so we need to convert it to list

my_list = list(city)
my_list.append("Mumbai")
print(my_list)
#or

a = (1,2,3,4)
b = a + (5,) #this is possible in int
print(b)

#Converting list to tuple

a = tuple (["a","b","c","d"])
print(a)

