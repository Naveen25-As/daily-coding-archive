# Insert a function that prints a greetings, and execute it on the p1 object.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is "+self.name)

p1 = Person("Naveen",19)
p1.myfunc()
