# Harshad(Niven) Number

num = int(input("Enter a number : "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit
    temp = temp // 10
    
if num % sum == 0:
    print(num, " is a Harshad number")
else:
    print(num, "is not a Harshad number")