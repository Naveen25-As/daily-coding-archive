# Write a Python program on Lambda functions with different methods.

print("Lamda function example")
# Auddition
add = lambda a,b: a+b
a = int(input("Enter a first number : "))
b = int(input("Enter second number : "))
result = add(a,b)
print("Result : ",result)
#Multiplication
mul = lambda c,d:c*d
c = int(input("Enter first number : "))
d = int(input("Enter second number : "))
result = mul(c,d)
print("result : ",result)
#list
numbers = [10,20,30,40,50]
print("Original numbers : ",numbers)
square_number = list(map(lambda n:n*n,numbers))
print("Square of numbers : ",square_number)