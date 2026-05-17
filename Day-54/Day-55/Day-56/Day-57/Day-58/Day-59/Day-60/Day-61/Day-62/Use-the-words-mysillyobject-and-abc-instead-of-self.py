# Use the words mysillyobject and abc instead of self.

class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfun(abc):
        print("Hello my name is "+abc.name)

p1 = Person("Naveen",19)
p1.myfun()
