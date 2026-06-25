# Pythom program for Voting Eligibilty using class and object.

class Voter:
    def __init__(self,age):
        self.age = age

    def check(self):
        if self.age >= 18:
            print("Eligible for voting")
        else:
            print("Not Eligible")

v = Voter(20)
v.check()
