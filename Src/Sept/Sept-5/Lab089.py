#Hierarchical Inheritance

class Father:
    def BHK1(self):
        print("1BHK house")

class Shylaja(Father):
    def BHK2(self):
        print("2 BHK house")

class Shravya(Father):
    def BHK3(self):
        print("3 BHK house")

class Sam(Father):
    def BHK4(self):
        print("4 BHK house")

Shyl = Shylaja()
Shyl.BHK1()
Shyl.BHK2()

shra = Shravya()
shra.BHK1()
shra.BHK3()