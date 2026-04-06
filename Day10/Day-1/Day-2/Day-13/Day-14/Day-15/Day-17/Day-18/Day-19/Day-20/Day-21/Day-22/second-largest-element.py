# Find second largest  element in list

numbers =[10,20,45,20,35]

largest = numbers[0]
second = numbers[0]

for i in numbers:
    if i >largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest number : ",second)