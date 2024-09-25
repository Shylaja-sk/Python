#example - abstract

from abc import ABC, abstractmethod

class Python(ABC):

    @abstractmethod
    def payfees(self):
        pass

    def enrolled(self):
        print("Enrolled")

class Shylaja(Python):
    def payfees(self):
        print("Paid")


s = Shylaja()
s.payfees()
s.enrolled()

