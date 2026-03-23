# Cheking Upper case ot lower case

ch = input("Enter a character: ")

if ch.isalpha():
    if ch.isupper():
        print("Upper case")
    else:
        print("Lower case")
else:
    print("It is not a character")