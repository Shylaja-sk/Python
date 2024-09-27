#Custom exception - user defined excecption

class MycustomEception(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)

balance = 100
withdraw = int(input("Enter the amount you want to withdraw\n"))
if withdraw > balance:
    raise MycustomEception("Balance is low")
else:
    print("Remaining bal",balance-withdraw)