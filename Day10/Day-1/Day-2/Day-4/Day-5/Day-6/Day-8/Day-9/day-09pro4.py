# print both even and odd

n = int(input("Enter a number : "))

print("Even numbers : ")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

print("Odd numbers : ")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)