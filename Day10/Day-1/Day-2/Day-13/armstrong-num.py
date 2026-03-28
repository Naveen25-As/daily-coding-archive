# check whether a number is armstrong 

num = int(input("Enter a number : "))
temp = num 
sum = 0

while num > 0:
    digit= num  % 10
    sum = sum + digit**3
    num = num // 10
if temp == sum:
    print("Armstrong number :")    # A number is Armstrong if the sum of the cubes of its digits equals the number itself.
else:
    print("Not a armstrong number")
    
# example output = 153