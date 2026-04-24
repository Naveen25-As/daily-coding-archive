# Increasing alphabet triangle in same alphabet in each row.

n = 4

for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end = " ")
    print()
