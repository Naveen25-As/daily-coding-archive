# Remove duplicate elements from a list

numbers = [1,2,3,2,4,1,5]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("List without duplicates : ",unique)