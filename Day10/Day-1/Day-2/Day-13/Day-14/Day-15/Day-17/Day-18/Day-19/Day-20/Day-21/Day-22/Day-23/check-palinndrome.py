# check palindrome or not

choice = input("Enter 'n' for number or Enter 's' for string : ")

if choice == 'n':
    num = int(input("enter a number: "))
    temp = num 
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    if num == reverse:
        print("Palindrome")
    else:
        print("Not a palidrome")

elif choice == 's':
    text = input("Enter a string : ")                                      
    reverse= ""
    for ch in text:
        reverse = ch + reverse
    if text == reverse:
        print("Palindrome")
    else:
        print("Not a Palindrome")
        
else:
    print("invalid choice")
    