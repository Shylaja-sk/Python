def outer_function():
    var1 = 30  # local int variable

    def inner_function():  # multiple inner function is possible
        print(var1)

    def inner_fun2():
        print(var1)

    inner_function()
    inner_fun2()


outer_function()
