# Example: Modify Object Properties

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ravi", 20)

print("Before Modification:")
print("Name:", s1.name)
print("Age:", s1.age)

s1.age = 22
s1.name = "Rahul"

print("After Modification:")
print("Name:", s1.name)
print("Age:", s1.age)
