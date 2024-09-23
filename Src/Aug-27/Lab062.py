#convert to lambda expression
import math


def sum_of_three_num(a,b,c):
    return a+b+c

result = sum_of_three_num(1,1,1)
print(result)

#using Lambda

result = lambda a,b,c : a+b+c
print(result(1,1,1))


#example

def find_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


find_even_odd(5)

#using lambda

check_even_odd = lambda num : "even" if num %2 ==0 else "Odd"
print(check_even_odd(10))


#example 2
def power(num):
    return math.pow(num,2)

a= power(2)
print(a)



power = lambda : math.pow(int(input("Enter the number")),2)
print(power())


