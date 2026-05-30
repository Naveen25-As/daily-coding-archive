# Python program to create a dictionary from keyboard and display the elements.

x = {}
n= int(input('How many elements?'))
for i in range(n):
    k = input("Enter key: ")
    v = int(input("Enter its value: "))
    x.update({k:v})

print("The dictionary is :",x)
