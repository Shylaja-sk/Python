# Polymorphism
# It is oops concept
# behaviour will be different based on who is calling
# Polymorphism allows objects of different classes to be treated as a object of a common super class
# to achive this - we have 2 types - method overloding and method over riding
#

# method Overridding - subclass have same name method as the parent or super class

class Shape:

    def area(self):
        print("print the areas of the shape")


class Rectangle(Shape):

    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width

    def area(self):
        return self.length + self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(3, 4)
print(shape1.area()) #first preference is given to local

shape2 = Circle(10)
print(shape2.area())
