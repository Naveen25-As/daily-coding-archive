# Program for calculater class using class and object.

class Calculator:
    
    def add(self,a,b):
        return a + b

    def sub(self,a,b):
        return a - b

c = Calculator()

print("Addition =",c.add(10,5))
print("Subtraction =",c.sub(10,5))
