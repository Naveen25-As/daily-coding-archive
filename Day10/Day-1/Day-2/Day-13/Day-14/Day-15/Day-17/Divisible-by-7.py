# Print all numbers divisibe by 7 from 1 to n

num = int(input("Enter a numebr : "))

print("Numbers divisible by 7 : ")

for i in range(1 , num + 1):
    if i % 7 == 0:
        print(i)
    