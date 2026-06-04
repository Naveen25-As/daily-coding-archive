# Example program for polymorphism.

class Birds:
    def sounds(self):
        print("Bird Sound")

class Parrot(Bird):
    def sound(self):
        print("Parrot Speaks")

p = Parrot()
p.sound()
