# Python program for Employee class.

class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Employee ID:",self.id)
        print("Name:",self.name)
        print("Salary:",self.salary)

# creating two objects
emp1 = Employee(101,"Naveen",30000)
emp2 = Employee(102,"Nikil",25000)

# Modifying salary of one employee
emp1.salary = 40000

# Display details
emp1.display_details()
print("-----------------")
emp2.display_details()
