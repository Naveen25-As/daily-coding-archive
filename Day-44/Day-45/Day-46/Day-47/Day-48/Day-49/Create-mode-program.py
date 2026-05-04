# Create mode program with exception handling.
try:
    file = open("newfile.txt","x")
    file.write("This is a new file created using x mode.")
    file.close()
    print("Create mode completed")
    
except FileExistsError:
    print("newfile.txt already exists")
    
