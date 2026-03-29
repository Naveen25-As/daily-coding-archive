# Print fabonacci series to n terms

n = int(input("Enter a number of terms : "))
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
    