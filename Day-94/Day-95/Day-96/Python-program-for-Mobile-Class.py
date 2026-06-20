# Python program for Mobile Class.

class Mobile:
    
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def show(self):
        print("Brand:",self.brand)
        print("Price:",self.price)

m = Mobile("Samsung",25000)
m.show()

    
