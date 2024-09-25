#Exception is a class
#Any event which disrupt the normal flow of a program when an error occurs
#They can raise from various situations, sunch as invalid operations and unexpexted condition
# Understanding how to handle exception is crucial for writing robust python code
#Error comes when there is syntax and logical error
#Execption it occurs during execution of the program

'''print(x) -- name error
print(10/0) -- ZeroDivisionError
print(1+"1") --TypeError
print(int('a')) -- ValueError

my_list=[1,2,3]
print(my_list[5]) --IndexError

while True print("Hello") --syntax error

   print("Hello world")'''

a = int(input("Enter the num1"))
b = int(input("Enter the num2"))
c = a/b #ZeroDivisionError: division by zero
print("result div is",c) #ValueError: invalid literal for int() with base 10: ' shy'


