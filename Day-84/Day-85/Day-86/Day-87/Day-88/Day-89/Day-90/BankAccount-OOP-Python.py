# Bank Account OOP Python.

class BankAccount:

    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def display(self):
        print("Balance=",self.balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.display()
