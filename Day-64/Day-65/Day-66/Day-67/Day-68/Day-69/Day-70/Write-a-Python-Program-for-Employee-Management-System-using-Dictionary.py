# Write a Python Program for Employee Management System using Dictionary.

employees ={}
while True:
    print("\n---Emloyee Menu---")
    print("1.Add Employee details")
    print("2.Search Employee")
    print("3.Display all Employees")
    print("4.Highest salary Employee")
    print("5.Exit")

    choice = int(input("Enter your choice:"))
    # 1.Add Employee.
    if choice == 1:
        eid = int(input("Enter Employee ID:"))
        name = input("Enter your name:")
        salary = input("Enter salary:")

        employees[eid] = {"name":name,"salary":salary}
        print("Employees added successfully")

    # 2.Search Employee.
    elif choice == 2:
        eid = int(input("Enter Employee to search:"))

        if eid in employees:
            print("Employee Found:",employees[eid])
        else:
            print("Employees NOT found")

    # 3.Display all Employees
    elif choice == 3:
        if len(employees) == 0:
            print("Employees not found")
        else:
            print("All Employees")
            for eid,data in employees.items():
                print("ID:",eid,"Name:",data["name"],"Salary:",data["salary"])
    #4.Check highest salary.
    elif choice == 4:
        if len(employees)== 0:
            print("No Employee records found")
        else:
            highest_id = max(employees,key = lambda e:employees[e]["salary"])
            highest = employees[highest_id]

            print("Highest Salary Employee")
            print("ID:",highest_id)
            print("Name:",highest["name"])
            print("Salary:",highest["salary"])

    elif choice == 5:
        print("Exiting program")
        break
    else:
        print("Enter valid choice")


            
                
            
    
          
