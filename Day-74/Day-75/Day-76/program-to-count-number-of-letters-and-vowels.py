# Program to count number of letters and vowels  

word = input("Enter a word:")
num_letters = len(word)
vowels = "aeiouAEIOU"
num_vowels = sum(1 for char in word if  char in vowels)
print("Number of letters:",num_letters)
print("Number of vowels:",num_vowels)
