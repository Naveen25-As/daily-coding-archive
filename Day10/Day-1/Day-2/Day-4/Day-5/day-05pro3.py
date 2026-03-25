#Average of numbers
n=int(input("How many time?"))
total=0
for i in range(n):
    num=int(input("Enter number:"))
    total=total+num
average=total/n
print("Average=",average)