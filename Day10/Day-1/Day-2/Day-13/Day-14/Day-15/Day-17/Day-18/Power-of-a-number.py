# Power of a number

base = int(input("Enter base number : "))
power = int(input("Enter power : "))

result = 1

for i in range(power):
    result = result * base

print("Result : ",result)