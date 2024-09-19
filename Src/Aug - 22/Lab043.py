#
# Task #11 -
# ✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

n = int(input("enter the size of fibancci series: "))
f1 = 0
f2 = 1
if n <= 0:
    print("The size of the series should be a positive integer.")
elif n == 1:
    print(f1)
else:
    # Print the first two numbers of the series
    print(f1, f2, end=" ")
    for i in range(n):
        sum = f1 + f2
        print(sum, end=" ")
        f1 = f2
        f2 = sum