# Finding the highest marks of the student

students = [
    (101,"Manu",94),
    (102,"Guru",84),
    (103,"Nikil",85),
    (104,"Naveen",99)
    
]

max_marks = students[0][2]

for s in students:
    if s[2] > max_marks:
        max_marks = s[2]
        
print("Heghest marks : ",max_marks)