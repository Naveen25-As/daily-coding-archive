# Read and write mode program.

file = open("demo3.txt","r+")

print("Reading file content:")
print(file.read())

file.seek(0,2)

file.write("\n This line is writed using read and write mode.")

file.close()

print("\n Data written successfully.")
