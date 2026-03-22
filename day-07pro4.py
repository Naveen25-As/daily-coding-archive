# Check vowel or consonant

ch = input("Enter a character:")

if ch.isalpha():
    if ch.lower() in ['a', 'e','i','o','u']:
        print( "Vowel")
    else:
        print("Consonant")

else:
    print("It is not character")