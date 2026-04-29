# Simple polymorphism program.

class Bird:
    def sound(self):
        print("Birds make sound")
class Dog:
    def sound(self):
        print("Dog barks ")

for animal in(Bird(),Dog()):
    animal.sound()
