# Python program for Product Discount using classand object.

class Product:
    
    def __init__(self,price):
        self.price = price

    def discount(self):
        final_price = self.price - (self.price * 10/100)
        print("Final Price:",final_price)

p = Product(5000)
p.discount()
