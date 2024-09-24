#Create calculator #Another way

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("Parameterized constructor")

    def sum(self):
        return self.a +self.b

    def subtract(self):
        return self.a - self.b

    def multi(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

result1 = Calculator(10,20)
result2 = Calculator(10,20)
result3 = Calculator(10,20)
result4 = Calculator(10,20)
output = result1.sum()
print(output)


