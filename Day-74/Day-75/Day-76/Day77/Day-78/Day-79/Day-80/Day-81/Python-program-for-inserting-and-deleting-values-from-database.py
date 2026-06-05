# Write a Python program for inserting and deleting values from database. 

import sqlite3

conn = sqlite3.connect("Student.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Student(
id INTEGER,
name TEXT
)
""")
cursor.execute(
    "INSERT INTO Student VALUES(2,'praveen')"
    )

conn.commit()

print("Records Inserted successfully")

cursor.execute(
    "DELETE FROM Student WHERE id = 2"
    )
print("Deleted successfully")
conn.commit()

conn.close()
