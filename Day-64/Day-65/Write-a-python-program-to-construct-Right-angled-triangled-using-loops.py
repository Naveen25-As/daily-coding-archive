# Write a python program to construct Right Angled Triangle using loops.

row = 5

for i in range(1,row+1):
    # print spaces
    for j in range(row-i):
        print(" ",end=" ")
    # Print stars
    for k in range(2*i-1):
        print("*",end=" ")
    print()
