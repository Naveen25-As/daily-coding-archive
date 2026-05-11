# Example program of class and object.

class Employee:
    def putdata(self):
        self.id = int(input("Enter employee id : "))
        self.name = input("Enter employee name : ")
        self.salary = int(input("Enter employee salary : "))

    def details(self):
        print("Employee Name: ",self.name)
        print("Employee ID: ",self.id)
        print("Employee Salary: ",self.salary)

a = Employee()
a.putdata()
a.details()


