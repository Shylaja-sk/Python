#Understanding Decorators in Python - used to modify the behavior of function or class without chaning it's source code
# They are powerful tool that allows  you to wrap another function and extend it's functionality while keeping the original functions code unchanged
# Code resusability, 
def add_extra_security(func):
    #two parts
    #@wrap and callable
    def wrapper():
        print("1. Something before function has called")
        print("2. helmate","knee gaurd")
        func()
        print("3.Something after function has called")
        print("4.rest","secure driving")
    return wrapper()

#defination
@add_extra_security
def driver():
    print("I'm driving")

@add_extra_security
def scooty():
    print("normal function")







