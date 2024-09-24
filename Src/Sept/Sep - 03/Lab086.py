#Multi-Level Inheritance

class Gradfather:
    gold = "2kg"

    def BHK1(self):
        print("1 BHK house")

class Father(Gradfather):
    dimond = "22 Karat"

    def BHK2(self):
        print("2 BHK house")


class Son(Father):
    btc = "1BTC"

    def BHK3(self):
        print("3 BHK House")


s = Son()
s.BHK1()

f = Father()
f.BHK2()
f.BHK1()

gf = Gradfather()
gf.BHK1()
gf.gold

