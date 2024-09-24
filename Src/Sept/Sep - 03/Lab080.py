class Car:
    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print ("Starting a car with name" + self.name)
        print ("Starting a car with Make" + self.make)
        print ("Starting a car with Model" + self.model)

Lambo = Car ("Lamborgini","V2","2024")
Lambo.start_engine()

I20 = Car ("I20","V6","2024")
I20.start_engine()