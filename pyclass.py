class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}, New Balance: {self.balance}")
        else:
            print("Deposit must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount!")

# Create accounts
acc1 = BankAccount("Mahesh", 1000)
acc2 = BankAccount("Sushan")

# Using methods
acc1.deposit(500)
acc1.withdraw(300)

# Checking account type
print(isinstance(acc1, BankAccount))  # True
print(isinstance(123, BankAccount))   # False
