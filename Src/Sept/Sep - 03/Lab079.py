class Person:
    #name = "Shylaja" #Hardcoded value -- so commenting


    def __init__(self,name,age):
        self.name = name #Instead we can use like this - constructor is used to change the instance variable during the object creation
        self.age = age

    def walk(self):
        return self.name


a = Person("Shylaja",20)
print(a.name)
b =Person("Shravya",20)
print(b.name)

print ("Who is walking with the object of a ", a.walk())

print(a.walk())





