# Write a program for Circle Area Program.

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(7)
print("Area of Circle :",c.area())
