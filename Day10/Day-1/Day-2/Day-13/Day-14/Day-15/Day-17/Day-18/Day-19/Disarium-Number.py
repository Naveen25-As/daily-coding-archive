# Disarium Number

num = int(input("Enter a number : "))

temp = num
digits = str(num)
length = len(digits)

sum = 0
for i in range(length):
    sum = sum + int(digits[i]) ** (i + 1)
    
if sum == num:
    print(num, "is a Disarium number")
else:
    print(num, " is  not a Disarium number")