#Class variable
# 1. Local Varible - within function or block
# 2. Global Varible
# 3. Instance Varible - within the class
# 3. Static Varible -


a = 10
class Person:
    b = 11 #Instamce belongs to class

    def print_info(self):
        global a
        a ="Hello"
        print(a)
        print(self.b)


a1 = Person()
a1.print_info()
#print(self.b) ---------we cannot use as it is instance variable