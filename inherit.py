class Bankac:
    def __init__(self,number,balance):
        self.balance=balance
        self.number=number

    def withdraw(self,amount):
        self.balance-=amount
    def __eq__(self, other):
        print("Bankac  __eq__ was called")
        return self.number==other.number


class Savingsac(Bankac):
    def __init__(self,number,balance,interest_rate):
        Bankac.__init__(self,number,balance)
        self.interest_rate=interest_rate

    def compute_interest(self, n_periods=1):
        return self.balance * ((1 + self.interest_rate) ** n_periods - 1)
    
    def __eq__(self, other):
        print("Savingsac __eq__ was called")
        return  self.number==other.number

    
class Checkingac(Bankac):
    def __init__(self,number,balance,limit):
        super().__init__(number,balance)
        self.limit=limit

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount,fee=0):
        if amount<=self.limit:
            Bankac.withdraw(self,amount+fee)
        else:
            # print("")
            pass

# ac=Savingsac(300,0.3)
# print(ac.compute_interest(2))
# print(ac.balance)
# bc=Checkingac(1000,500)
# bc.withdraw(400)
# print(bc.balance)

np=Bankac(300,123)
ind=Savingsac(300,123,0.1)
print(np==ind)  #python will always call child eq method




        