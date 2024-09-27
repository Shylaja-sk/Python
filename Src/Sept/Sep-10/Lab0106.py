class ABC:

        try:
            a = int(input("Enter the num1"))
            b = int(input("Enter the num2"))
            c = a / b  # ZeroDivisionError: division by zero
            print("result div is", c)  # ValueError: invalid literal for int() with base 10: ' shy'
        except ValueError as ve:  # as is alias
            print(ve)
            print("You have enetred the string, we want interger")

a = ABC()
a.c