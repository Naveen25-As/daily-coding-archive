# Nested if else program

age = int(input("Enter your age : "))
country = input("Enter your country name :")
if age >= 18:
    if country == 'indian':
        print("Your are elegible to vote ")
    else:
        print("Your are not a indian citizen so you cannot vote her.")

else:
    print("You cannot vote your age is below '18'")



