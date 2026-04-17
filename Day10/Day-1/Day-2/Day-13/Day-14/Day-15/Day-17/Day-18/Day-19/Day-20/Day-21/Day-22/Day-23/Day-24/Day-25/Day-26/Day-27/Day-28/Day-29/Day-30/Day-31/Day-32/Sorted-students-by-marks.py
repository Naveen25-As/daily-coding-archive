# Sorted students by marks

students=[
    (101,"manu",94),
    (102,"nikil",91),
    (103,"naveen",95),
    (104,"ritvik",90)
]

sorted_studetds = sorted(students,key=lambda x:x[2],reverse=True)

print("Students sorted by marks (Highest first):")
for s in students:
    print(s)