class Bankac:
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        self.balance-=amount

class Savingsac(Bankac):
    def __init__(self, balance,interest_rate):
        Bankac.__init__(self,balance)
        self.interest_rate=interest_rate

    def compute_interest(self, n_periods=1):
        return self.balance * ((1 + self.interest_rate) ** n_periods - 1)
    
class Checkingac(Bankac):
    def __init__(self, balance,limit):
        super().__init__(balance)
        self.limit=limit

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount,fee=0):
        if amount<=self.limit:
            Bankac.withdraw(self,amount+fee)
        else:
            # print("")
            pass

ac=Savingsac(300,0.3)
# print(ac.compute_interest(2))
# print(ac.balance)
bc=Checkingac(1000,500)
bc.withdraw(400)
print(bc.balance)




        