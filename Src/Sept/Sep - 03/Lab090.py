#Hybrid - Mixture of multiple and hierachical

#Interview

class A:
    def methodA(self):
        return "Method A"


class B(A):
    def methodB(self):
        return "Method B"

class C(A):
    def methodC(self):
        return "Method C"

class D(B,C): #D can use everything

    def methodD(self):
        return "Method D"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())