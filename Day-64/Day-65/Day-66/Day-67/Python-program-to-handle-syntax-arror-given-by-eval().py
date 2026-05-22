# Python program to handle syntax arror given by eval().

try:
    result = eval(input("Enter expression:"))
    print("Result:",result)

except SyntaxError:
    print("Syntax Error occured")
