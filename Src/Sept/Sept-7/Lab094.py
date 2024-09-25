#Method Overloading
#Python does not support method overloading
#Same method name with different work


class addition(object): #Object is a super class for all the classes by default even if we don't type

    def add(self,a,b):
        return a+b

    def add(self, a, b,c=0): #It will work only when default value is assigned
        return a+b+c

    def add(self, a, b,c=0,d=0): #It will work only when default value is assigned
        return a+b+c+d


Sum = addition()
Sum = Sum.add(10,20) #python interpreter is confused as in which menthod to call
print(Sum)