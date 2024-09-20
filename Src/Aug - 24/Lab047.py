#No return type with defaul arg

def greet_by_name(name="Shylaja"):
    print("Hello", name.upper())



greet_by_name("Shravya")
greet_by_name()
greet_by_name(name="Sam") #positional argument


def muilty_arg(name1,name2,name3):
    print("Hello,", name1,name2,name3)

muilty_arg("Shylaja","Amma","sam")


#Arg with return type

def sum_of_2_nums(num1,num2):
    return num1+num2
result=sum_of_2_nums(10,20)

print(result)
#sum_of_2_nums() - not possible as default arg is not available