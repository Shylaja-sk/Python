class Parent:
    gold = "2kg"
    print("2kg gold")

    def BHK2(self):
        print("2BHK house")

class Child(Parent):
    def BHK3(self):
        print("3BHK house")


child_obj = Child()
child_obj.gold
child_obj.BHK2()
child_obj.BHK3()

parent_obj = Parent()
parent_obj.BHK2()

# parent_obj.BHK3() - not possible


