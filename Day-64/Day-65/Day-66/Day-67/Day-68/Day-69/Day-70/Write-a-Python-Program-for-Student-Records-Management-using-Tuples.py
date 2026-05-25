# Write a Python program for student reacords Management using tuples.

students = [
    (101,"Naveen",95),
    (102,"Kavya",95),
    (103,"Nikil",92),
    (104,"Sneha",85),
    (105,"Bindu",90)
 ]


# 1.Display all students records
print("Students records:")
for s in students:
    print(s[0],s[2])

#2.Find highest marks.
max_marks = students[0][2]

for s in students:
    if s[2] > max_marks:
       max_marks = s[2]

# 3.Find all toppers
toppers = []
for s in students:
    if s[2] == max_marks:
       toppers.append(s)
# 4.Sort students by marks(descending)to assign ranks
sorted_students = sorted(students, key = lambda x:x[2],reverse = True)

# 5. Search students find rank.
roll = int(input("\n Enter Rolll Number to search:"))
found = False

rank = 1
prev_marks = None
actual_rank = 0

for i in range(len(sorted_students)):
    if prev_marks != sorted_students[i][2]:
       actual_rank = rank
    prev_marks = sorted_students[i][2]
    if sorted_students[i][0] == roll:
       print("Students Found:",sorted_students[i])
       print("Rank",actual_rank)
       
       if sorted_students[i][2] == max_marks:
           print("This student is a Topper")
       else:
           print("This student is NOT a Topper")

       found = True
       break
    rank += 1
if not found:
    print("Student not found")

                 
     
                             
