# Python program for ATM Simulation using class and object.

class ATM:
    
    def __init__(self,balance):
        self.balance = balance
        
    def withdraw(self,amount):
        
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")
            
        print("Available balance =",self.balance)

a = ATM(10000)
a.withdraw(2500)
