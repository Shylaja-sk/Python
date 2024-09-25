#Errors are something difficult to handle
# error are more sever issues that tipically
#exception can be handled

#Try , except, Finnally


try:
    a = int(input("Enter the num1"))
    b = int(input("Enter the num2"))
    c = a/b #ZeroDivisionError: division by zero
    print("result div is",c) #ValueError: invalid literal for int() with base 10: ' shy'
except ValueError as ve: #as is alias
    print(ve)
    print("You have enetred the string, we want interger")
except ZeroDivisionError as ze:
    print(ze)
    print("Zero div error, don't use num2 as 0")
else:
    print("Print Result")

finally:
    print("This code will be always executed")