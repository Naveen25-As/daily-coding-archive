# Write a program to create, append, and remove lists in Python.

number = [10,20,30,40,50]

# Append operation
add_num = int(input("Enter a number : "))
number.append(add_num)
print("list after append",number)

# Remove operation
remove_num = int(input("Enter a number : "))
number.remove(remove_num)
print("List after remove : ",number)