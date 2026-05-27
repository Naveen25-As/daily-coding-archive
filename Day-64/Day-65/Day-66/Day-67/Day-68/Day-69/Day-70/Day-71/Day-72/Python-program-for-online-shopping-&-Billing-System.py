# Write a Python program for online shopping & Billing System using variable length and default arguments.

def shopping_system(customer_name,*items,discount=0,delivery="standard",**details):
    print("\n---Bill---")
    print("Name:",customer_name)

    if details:
        for key,value in details.items():
            print(key,":",value)
    total = 0

    if items:
        for name,price in items:
            print(name, "-" ,price)
        total += price

    else:
        print("No items")

    if discount > 0:
        d = total * discount*100
        total -= d
        print("Discount:",discount,"%")

    print("Delivery:",delivery)
    print("Total:",total)
    print("-------")
shopping_system("Rahul",("shirt",5000),("Shoes",1500),dicount=10,delivery="express",city ="hubli")
shopping_system("manu",("pen",10),city="belegav")
shopping_system("nikil")














