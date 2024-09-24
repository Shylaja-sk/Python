#Encapsulation - Public, Private, protected
#bind the data variables and methods
#methods - function which we can created
#Hide the data members (class, instance vafriables) by using methods
#by using only methods


class Myclass:
    #public variable = members are accessble from anywhere in the program - everywhere
    public_var = "I am public"
    balance = 123

    #Private variable = scope is within the class only
    __private_var = "I am Private"

    #Proted variable = members are intended for internal use within the class and it's subclasses - within the package
    _protected_var = "I am Protected"



obj_var = Myclass()
print(obj_var.public_var, obj_var.balance)
#print(obj_var.__private_var) cannot access
print(obj_var._protected_var)




