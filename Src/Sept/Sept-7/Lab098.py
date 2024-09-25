#Static method- it belongs to a class rather than an instance of the class rather than an instance of the class

class MathOperation:


    def div(self,a,b):
        return a/b

    @staticmethod #we can create multiple methods
    def sum(a,b):
        return a + b



o = MathOperation()
output = o.div(10,20)
print(output)
print(MathOperation.sum(10,20)) #directly we can call for static method,


