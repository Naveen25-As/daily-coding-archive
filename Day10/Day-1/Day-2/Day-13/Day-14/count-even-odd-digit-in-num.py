# Count even odd digit in a number

num = int(input("Enter a number : "))
even = 0
odd = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    num = num // 10

print("Even digit : ",even)
print("Odd digit : ",odd)