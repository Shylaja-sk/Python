#Inheritance
#If we want to aquare attributes and methods from another class
#child can inherit the attrubutes from parent and methods

#Types
#1. single inheritance - 80% used
#2. multiple inheritance
#3. multi level inheritance
#4. hybrid inheritance
#5. hierachical inheritance

class Father: #father cannot access child 
    key = "2BHK"

    def car(self): #self is reference current object - default parater in function we can access instance variable
        print("Father car",self.key)

class Son(Father):
    pass

Father_obj = Father()
Father_obj.car()

son_obj = Son()
son_obj.car()


