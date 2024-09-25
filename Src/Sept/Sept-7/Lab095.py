#Oops concepts
#1. Class - Bluepreint
#Object - Instance of class
#Encapsulation --> _Private, public , __protected - Hiding internal
#Inheritance - Single, multiple, multi-level, hieracical, and Hybrid
#Polymorphism - Method overriding -- with multiple class and Method overloading (not supported) --within the class
#Self, Super(), __init__() --> constructor
#Abstraction

#Abstraction - Hide the details and show what is required - Hiding in class level - other class

from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def sound(self): #This is incomplete method and somebody has to complete it
        pass

class Dog(Animal):

    def sound(self): #It has to override and complete the method
        print("Bark")

dog1 = Dog("AA")
dog1.sound()






