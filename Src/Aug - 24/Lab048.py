#create a prg sum of 3 numbers from users

num1 = int(input("Enter number 1 \n"))
num2 = int(input("Enter number 2 \n"))
num3 = int(input("Enter number 3 \n"))

def sum_of_3_nums(n1,n2,n3):
    return n1+n2+n3
results= sum_of_3_nums(num1,num2,num3)
print(results)
results= sum_of_3_nums(n1=num1,n2=num2,n3=num3)
print(results)


