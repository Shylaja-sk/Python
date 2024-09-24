#Web automation - Selenium
#Page - you are gping to automate

class VWOLoginpage:


    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "shylaja@gmail.com" and self.password == "pass":
            print ("Allowed to login")
        else:
            print ("Not allowed to login")

email = input("Enter the email\n")
password = input("Enter the password\n")

vwo_obj = VWOLoginpage (email,password)
vwo_obj.login_confirm()


