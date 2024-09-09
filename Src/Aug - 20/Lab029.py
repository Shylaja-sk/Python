# Find the max btw 3 numbers
30
num2 = float(input("Enter the 2nd number\n"))
num3 = float(input("Enter the 3rd number\n"))
num1 = float(input("Enter the 1st number\n"))
print(max(num1, num2, num3))

if num1 > num2:
    print(num1, "is greater")
elif num1 > num3:
    print(num1, "is greater")
else:
    print(num3, "is greater")

# or

if num1 > num2 and num1 > num3:
    print(num1, "is greater")
elif num2 > num1 and num2 > num3:
    print(num2, "is greater")
else:
    print(num3, "is greater")

