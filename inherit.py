class Bankac:
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        self.balance-=amount

class Savingsac(Bankac):
    pass

ac=Savingsac(200)

print(isinstance(ac,Bankac))


        