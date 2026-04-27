# Simple encapsulation program.

class student:
    def __init__(self):
        self.__marks = 90
    def show(self):
        print("Marks : ",self.__marks)
s1 = student()
s1.show()
