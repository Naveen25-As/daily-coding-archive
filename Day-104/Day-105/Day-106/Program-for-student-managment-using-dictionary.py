# Program for student managment using dictionary.

student ={}
while True: 
    print("1.Add Student Details.")
    print("2.Display all Student Details.")
    print("3.Search student.")
    print("4.Exit")
    
    ch = int(input("Enter your choice(1-4):"))
    
    if ch == 1:
        sid = int(input("Enter student ID:"))
        name = input("Enter student name:")
        age = int(input("Enter student age:"))
        marks = float(input("Enter marks:"))
        student[sid]={"Name":name,"Age":age,"Marks":marks}
        print("Student details added successfully")
    elif ch == 2:
        if (len(student))==0:
            print("No student details")
        else:
            print("Student details")
            for sid, details in student.items():
                print("ID:", sid)
                print("Name:", details["Name"])
                print("Age:", details["Age"])
                print("Marks:", details["Marks"])
                
                
    elif ch == 3:
        if (len(student))==0:
            print("Students are not found")
        else:
            sid = int(input("Enter student id to search:"))
            if sid in student:
                print("Student found:",student[sid])
            else:
                print("Student not found!")
    elif ch == 4:
        print("Exit")
        break
    else:
        print("Enter valid choice")
        
                
                
        
