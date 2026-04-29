# Simple inheritance program.

class person:
    def show(self):
        print("I am the persion")

class student(person):
    pass               # Show nothing for now


s = student()
s.show()
