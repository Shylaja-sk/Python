# Function scope

global_b=20 # Global variable
def my_fun():
    age = 10 #Local variable within the function
    print(age)
    global_b=30 #reinitailizing the value
    print(global_b) #possible

def f1():
    print(global_b) # Global variable can be access in another function as well

my_fun()
print(global_b) #possible -  Reinitializing will not reflect here, becuase it is within a function
f1()



