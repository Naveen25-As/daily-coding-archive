# Remove duplicate elements from list 

numbers  = [1,2,3,4,2,1,5]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)
        
print("List without duplicates : ",unique)