#In Python we can create 2 dir
#1. Normal dir
#2. package - right click create package --> __init__.py -- you can call the ptython which is present in this dir to other dir

#To take user input to create a class
class Person:
    def __init__(self):
        self.name = input("Enter the name\n")
        self.age = input("Enter the age\n")
        self.phone = input("Enter the Phone\n")
        self.occupation = input("Enter the occupation\n")


    def display(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Phone is {self.phone}")
        print(f"Occupation is {self.occupation}")

#Create an object
person1 = Person()
#call display function
person1.display()