# Selecting a course in a college

print("Welcome to our 'P C Jobin College' ")
print("Our courses are here given below : ")
course = [
    (1,"BCA"),
    (2,"MCA"),
    (3,"BSC"),
    (4,"MSC")
]
print(course)
c = int(input("Enter your choice (1-5): "))

if c == 1:
    print("Your choice is BCA")
    name = input("Enter your name : ")
    print(name,"choice is BCA")
elif c == 2:
    print("Your choice is MCA")
    name = input("Enter your name : ")
    print(name,"choice is MCA")
elif c == 3:
    print("Your choice is BSC")
    name = input("Enter your name : ")
    print(name,"choice is BSC")
elif c == 4:
    print("Your choice is MSC")
    name = input("Enter your name : ")
    print(name,"choice is MSc")

else:
    print("invalid choice !")