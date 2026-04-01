# Find the sum oof even numbers from 1 to N

n = int(input("Enter a number : "))
sum = 0

for i in range(1 , n + 1):
    if i % 2 == 0:
        sum = sum + i
 
print("Print sum of even numbers : ",sum)