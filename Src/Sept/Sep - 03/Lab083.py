#example
# a - public
# _a - protected
# __a - Private

class Bank:
    def __init__(self,account_number,balance):
        self.balance = balance
        self.__account_number = account_number
        self.check_balance()

    def deposit(self,amount):
        self.balance = self.balance+amount

    def check_balance(self):
        print(self.balance)



    def account_number(self,isauth): #This fuction public in nature, so it is able to access the private variable as it is within the class
        if isauth == True:
            print(self.__account_number)
        else:
            print("Not allowed")

    def __internal(self): #private method advantage is it can access private variable as well as it can access public method ----- They cannot be called but can be used internally
        print("This is Private method")
        self.account_number()
        self.check_balance()
        self.deposit()


icic = Bank(654654654564,100)
#icic.__init__ -- it cannot be called directly
icic.deposit(100)
icic.deposit(100)
icic.check_balance()
print(icic.account_number(True))



