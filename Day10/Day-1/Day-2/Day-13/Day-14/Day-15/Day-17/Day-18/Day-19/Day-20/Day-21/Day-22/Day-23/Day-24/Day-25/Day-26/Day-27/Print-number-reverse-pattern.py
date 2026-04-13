# Print number reverse pattern

row = 4
for i in range(row,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()