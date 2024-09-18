#task07
# #Leap year checker
#create a program that determines whether a given year is leap year.
#A leap year is divisble by 4,but not by 100 unless it is also divisible by 400.

Year=int(input("Enter the year:"))
if (Year%4==0 and Year%100!=0) or (Year%400==0):
    print(f"Year {Year} is a leap year")
else:
    print(f"Year {Year} is  not a leap year")