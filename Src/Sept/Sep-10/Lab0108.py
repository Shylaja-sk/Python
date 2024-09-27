
balance = 100
withdraw = int(input("Enter the amount you want to withdraw\n"))
if withdraw > balance:
    print("Low balance")
else:
    print("Remaining bal",balance-withdraw)