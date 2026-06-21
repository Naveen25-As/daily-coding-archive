# Program for Laptop Class.

class Laptop:
    
    def __init__(self,company,ram):
        self.company = company
        self.ram = ram
    def display(self):
        
        print("Company:",self.company)
        print("Ram:",self.ram,"GB")
        
l = Laptop("HP",16)
l.display()
