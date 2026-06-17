# Python program for Simple Interest.

class Interest:
    def __init__(self,p,r,t):
        self.p = p
        self.r = r
        self.t = t

    def calculate(self):
        si = (self.p * self.r * self.t) / 100
        print("Simple Interest = ",si)

obj = Interest(10000, 5, 2)
obj.calculate()

