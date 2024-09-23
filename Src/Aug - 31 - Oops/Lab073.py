#Constructor
#Special function in class, __init__()
# It will be automatically called when you create an object
# When object is created --> constructor is called automatically
# we can have unlimted arguments
#2 types - default with no arguments and parameterized with arguments
# does not return anything
#__init__  name of the constructor
#purpose is to assign thr values


class Dog:
    name = None
    age = None


    def sleep(self):
        print("Sleeping "  +self.name,self.age)

    def barking(self):
        print("Barking")

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("I will be automatically called when you create an object")

dog1 = Dog("Chow chow",10)
print(dog1.name )
dog1.sleep()

