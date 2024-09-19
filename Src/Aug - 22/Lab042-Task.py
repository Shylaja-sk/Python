
# Task #10 -
# Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

Num=int(input("Enter the number to find  a factorial:"))
fact=1;
i=Num
while i>=1:
    fact=i*fact
    i=i-1
print(f"Factorial of {Num}! is: ",fact)