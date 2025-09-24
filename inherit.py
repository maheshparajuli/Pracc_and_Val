class Bankac:
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        self.balance-=amount

class Savingsac(Bankac):
    def printall(self):
        print("whats going")

ac=Savingsac()
isinstance(ac,Bankac)
        