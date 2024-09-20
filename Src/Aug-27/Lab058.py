#Understanding Decorators in Python - used to modify the behavior of function or class without chaning it's source code
# They are powerful tool that allows  you to wrap another function and extend it's functionality while keeping the original functions code unchanged
# Code resusability,
def running_UI(custom_func_to_get_extra_functionality):
    #two parts
    #@wrap and callable
    def wrapper():
        print("1. Open application ")
        print("2. Execute the tescases")
        custom_func_to_get_extra_functionality()
        print("3.validate the results")
        print("4.Quit browser")
    return wrapper()

#defination
@running_UI
def test_Ui1():
    print("I'm testing")

@running_UI
def test_Ui2():
    print("Testing 2nd application now")







