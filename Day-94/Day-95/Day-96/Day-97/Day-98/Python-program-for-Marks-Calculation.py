# Python program for Marks Calculation.

class Marks:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        print("Total Marks =",self.m1 + self.m2 + self.m3)

s = Marks(80,75,90)
s.total()
