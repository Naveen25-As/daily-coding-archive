# Program for Electricity Bill.

class ElectricityBill:
    
    def __init__(self, units):
        self.units = units

    def calculate(self):
        bill = self.units * 5
        print("Bill Amount=",bill)
        
e = ElectricityBill(120)
e.calculate()
