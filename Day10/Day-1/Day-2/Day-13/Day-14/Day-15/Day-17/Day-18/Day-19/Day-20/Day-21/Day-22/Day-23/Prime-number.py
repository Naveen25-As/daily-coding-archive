# Write a Python script that prints prime numbers less than 30.

print("Print numbers less than 30 are : ")
for num in range(2,30):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num, end = " ")
    