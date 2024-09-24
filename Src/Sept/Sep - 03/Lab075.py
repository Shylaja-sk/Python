#Create calculator

class Calculator:
    def __init__(self):
        print("Default constructor")

    def sum(self, a,b):
        return a + b

    def subtract(self, a,b):
        return a - b

    def multi(self, a,b):
        return a * b

    def div(self, a,b):
        return a / b


'''reference = Calculator()
output1 = reference.sum(10,20)
output2 = reference.subtract(10,20)
output3 = reference.multi(10,20)
output4 = reference.div(10,20)

print(output1,output2,output3,output4)'''


#or


reference = Calculator()
a = float(input("Enter value for A"))
b = float(input("Enter value for B"))
output1 = reference.sum(a,b)
output2 = reference.subtract(a,b)
output3 = reference.multi(a,b)
output4 = reference.div(a,b)

print(output1,output2,output3,output4)

