# Application of scholarship program.

name = input("Enter your name :")
marks = int(input("Enter your marks (out of 100):"))
income = int(input("Enter your income:"))
caste = input("Enter your caste(Sc/St/Obc/Others):").lower()
sports = input("Your are a sports person(yes/no):").lower()

if marks >= 70:
    print("You are elegible for scholarship.")
    if income < 500000:
        print("Your are eligible.")
        if caste == "sc" or caste == "st":
            print("Your are eligible for extra scholarship.")
        elif caste == "obc":
            print("Your are eligible for best scholarship.")
        else:
            print("Your are not eligible due to the upper caste.")
        if sports == "yes":
            print("You can get high scholarship.")
        elif sports == "no":
            print("You are not eligible for high scholarship.")
        else:
            print("Please enter 'yes' or 'no'.")
    else:
       print("Your are not eligible for government scholarship.")
else:
    print("You are not eligible for scholarship.")

    
