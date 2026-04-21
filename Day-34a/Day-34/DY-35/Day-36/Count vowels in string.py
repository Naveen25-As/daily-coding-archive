# Count vowels in string

string =  input("Enter a string :")

vowels = "aeiouAEIOU"
count = 0
for ch in string:
    if ch in vowels:
        count += 1

print("Number of vowels :",count)
