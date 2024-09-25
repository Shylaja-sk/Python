#Try Catch - when there is error in Try metjod tit will start executing the except method

print("Start of the program")
try:
    a = int(input("Enter the num1"))
    b = int(input("Enter the num2"))
    c = a/b #ZeroDivisionError: division by zero
    print("result div is",c) #ValueError: invalid literal for int() with base 10: ' shy'
except Exception as e: #as is alias
    print(e)
    print("Please check your input it should not be string or 0")
print("---End of the program")


