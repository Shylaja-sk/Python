#Method overriding - example
#same name in parent and child
#super means call my parent function


class Father:

    a=10
    def home(self):
        print("1BHK")
        print(self.a) #if we have to print it's own varaiale then self is required
class Son(Father):
    b=20
    def home(self):
        super().home() #my parent home - super get the above class
        print(super().a) #we can also access the variable and it is used within the class
        print("No House")
        print(self.b) # Self is my variable and Super is parent or super class to get the data


shylaja = Son()
shylaja.home()

