# Find the power o a number (x^y)

x=int(input("Enter base base number : "))
y=int(input("Entr power : "))

result = 1
for i in range(y):
    result = result * x
print("Result : ",result)
