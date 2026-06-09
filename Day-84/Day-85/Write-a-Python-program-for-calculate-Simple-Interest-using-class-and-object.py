# Write a Python program for calculate Simple Interest using class and object.

class Interest:
    def __init__(self,p,r,t):
        self.p = p
        self.r = r
        self.t = t

    def calculate(self):
        si = (self.p * self.t * self.r) / 100
        print("Simple interest=",si)
obj = Interest(10000,5,2)
obj.calculate()
