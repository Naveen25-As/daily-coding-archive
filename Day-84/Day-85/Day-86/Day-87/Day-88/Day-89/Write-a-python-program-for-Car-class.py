# Write a python program for Car class.

class Car:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)

c1 = Car("Hyundai","i20")
c1.display()

