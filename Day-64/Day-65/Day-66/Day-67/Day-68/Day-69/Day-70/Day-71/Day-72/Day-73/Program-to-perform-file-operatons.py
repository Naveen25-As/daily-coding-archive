'''Write a python program to perform the following file operations 
i. Open file in write and binary mode
ii. Display file name 
iii. Write Text to file 
iv. To read from the file '''

f1 = open(r"C:\Users\navee\OneDrive\Pictures\dream bike.webp","rb")
f2 = open("copyingimage.png","wb")
bytes = f1.read()
f2.write(bytes)
f2.close()
f1.close()

print()
print("File name:",f1.name)
print()

f = open("myfile.txt","a")
str = input("Enter text:")
f.write(str)
f.close()

f = open("myfile.txt","r")
str = f.read()
print("Reading text from file is:",str)
f.close()
