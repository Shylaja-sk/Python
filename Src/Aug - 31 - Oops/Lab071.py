#A class contains attributes and methods

class person:
    #attributes
    id = None
    email = None
    name = None
    age = None
    gender = None
    address = None

    #behaviour
    def talk(self): #self -- this --will be fisrt argument in every behaviour and no return type and no argument
        print("I can talk")

    def sleep(self,name):
        print("I'm a method")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self):
        return "I am walking"

#create an object of the class
#object reference = classname()

a1 = person()
a1.name = "Shylaja"
print(a1.name)



