'''If exceptions are not handled properly, our programs halts. Exception handling is the concept of preventing the program 
from terminating when an exception is raised. we use try-except-finally sequence to catch an exception and handle it.

Sometimes, we want to raise exceptions ourselves.
look at following example:

def list_of_ones(length):
    if length<=0:
        raise ValueError("invalid length.)
    return [1]*length

There are classes and subclasses of exceptions.
one hiearchy is BaseException/Exception/ArithmeticError/ZeroDivisonError

Also, we can make custom exceptions by inheriting from built-in exception classes/subclasses.
Look this example:


class BalanceError(Exception):
    pass

class Customer:
    def __init__(self,balance):
        if balance<0:
            raise BalanceError("balance has to be non-negative.")
        else:
            self.balance=balance

'''

try:
    print('a'+5)
except TypeError:
    print("You can't add integer to the string,but can multiply them")
finally:
    print('a'*5)