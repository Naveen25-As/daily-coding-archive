# Write a Python Program for Student Scholarship Eligibility using Nested-If.

name = input("Enter your name:")

marks = float(input("Enter your marks:"))
income = float(input("Enter your income:"))
attendence = int(input("Enter your attendence percentage:"))
categary = input("Enter your categary:").lower()
sports = input("Sports(yes/no):").lower()

if marks < 60:
    print("Not elegible low marks")
elif attendence < 75:
    print("Not elegible Low attendence")
elif income > 50000:
    print("NOt elegible High income")
else:
    print("Your are elegible for scholarship")

    if marks >= 90:
        print("high scholarship")
    elif marks >= 75:
        print("Standard scholarship")
    else:
        print("Basic scholarship")

    if sports == "yes":
        print("Your are elegible for sports scholarship")
    else:
        print("Not elegible for sports scholarship")

    if categary in ["sc","st"]:
        print("High ")
    elif categary == "obc":
        print("Standard ")

print("Thank you")







            
