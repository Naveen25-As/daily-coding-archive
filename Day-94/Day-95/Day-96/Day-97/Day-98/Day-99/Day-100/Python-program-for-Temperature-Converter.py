# Python program for Temperature Converter.

class Temperature:
    
    def __init__(self,celsius):
        self.celsius = celsius

    def fahrenheit(self):
        f = (self.celsius * 9/5) + 32
        print("Temperature in Fahrenheit: ",f)


t = Temperature(30)
t.fahrenheit()
