#Multiple Inheritance
#
class Father():
    __password = "123"

    def __show_password(self):
        print(self.__password)

    def father_money(self):
        return 5
    def home(self):
        return "This is from Father"

    def show_everything(self):
        self.__show_password()

class Mother:

    def mother_money(self):
        return 2

    def home(self):
        return "This is from Mother"


class Son(Father,Mother):
    pass

s = Son()
print(s.father_money())
print(s.mother_money())
print(s.home()) #in java we have a problem in this case to which home it should call - it is called Diamond problem- But in Python do not have this problem instead it will take
#the first argument - simce it is father it has taken father or if mother is in 1st arg it will take mother's home - method resolution order
#Note** if Son has some value in that case it will give preference to it's own value
s.show_everything()





