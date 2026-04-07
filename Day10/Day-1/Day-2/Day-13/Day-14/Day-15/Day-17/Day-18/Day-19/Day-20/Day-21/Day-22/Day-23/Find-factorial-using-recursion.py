# Write a python program to find factorial of a number using recursion. 

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fact(n-1)
n= int(input("Enter a number : "))
print("Number : ",n)
print("Factorial : ",fact(n))