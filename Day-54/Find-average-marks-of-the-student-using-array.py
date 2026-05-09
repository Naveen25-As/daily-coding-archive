# Find average marks of the student using array.

marks =[]
n =3
for i in range(6):
    val = int(input("Enter values:"))
    marks.append(val)

print("Marks are:",marks)
average = sum(marks) / len(marks)
print("Average : ",average)
