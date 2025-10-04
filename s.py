"""Remainder: module is single .py file, package is collection of modules.
Analogy:
Euta book = MODULE
Euta bookshelf = Package




import datetime
import time


def log_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        print(f"[START] {func.__name__} at {start.strftime('%Y-%m-%d %H:%M:%S')}")

        result = func(*args, **kwargs)

        end = datetime.datetime.now()
        duration = (end - start).total_seconds()
        print(f"[END] {func.__name__} at {end.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"[DURATION] {func.__name__} took {duration:.2f} seconds\n")
        # return result
    return wrapper


@log_time
def slow_task():
    print("Running slow task...")
    time.sleep(2)

@log_time
def fast_task():
    print("Running fast task...")
    time.sleep(0.5)


slow_task()
fast_task()
"""

"""
class Parent:
    def __init__(self):
        self.parent_attribute = 'I am a parent'

    def parent_method(self):
        print('Back in my day...')



class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.child_attribute = 'I am a child'



child = Child()


print(child.child_attribute)
print(child.parent_attribute)
child.parent_method()

"""





"""multiple inheritance: taking features from many classes, two or more than two.
.get(key, default) is a dictionary method that tries to fetch the value for the given key.
"""

class Person:
    def __init__(self,name,phone_no):
        self.name=name
        self.phone_no=phone_no

    def display_info(self):
        return f"NAME:{self.name}\
            PHONE NUMBER: {self.phone_no}"
    
class Customer(Person):
    def __init__(self,name,phone_no,address):
        super().__init__(name,phone_no)
        self.address=address

    def display_cust(self):
        return f" {self.display_info()} \
             ADDRESS: {self.address} "

class Restaurant:
    def __init__(self):
        self.menu={
            "Veg momo":120,
            "Chicken momo": 180,
            "Anda Fry":40,
            "Chau Chau sadeko":50
        }

    def show_menu(self):
        print("\n ****MENU****")
        for item,price in self.menu.items():
            print(f"{item}: RS. {price}")

        def get_price(self,item):
            return self.menu.get(item,None)
        
class Order(Customer,Restaurant):
    def __init__(self,name,phone_no,address):
        Customer.__init__(self,name,phone_no,address)
        Restaurant.__init__(self)
        self.cart=[]

    def add_item(self, item, quantity):
        price = self.get_price(item)
        if price:
            self.cart.append((item, quantity, price * quantity))
            print(f"Added {quantity} x {item} to cart.")
        else:
            print("Item not found in menu!")
    
    def show_cart(self):
        print("\n--- Your Cart ---")
        total = 0
        for item, qty, cost in self.cart:
            print(f"{item} ({qty}) - Rs {cost}")
            total += cost
        print(f"Total Bill: Rs {total}")
        return total



print("Welcome to Food Ordering System")


name = input("Enter your name: ")
phone = input("Enter your phone number: ")
address = input("Enter your address: ")


order = Order(name, phone, address)

print("\nCustomer Details:")
print(order.display_customer())


order.show_menu()

while True:
    choice = input("\nEnter food item to add (or 'done' to finish): ").title()
    if choice.lower() == "done":
        break
    qty = int(input(f"Enter quantity of {choice}: "))
    order.add_item(choice, qty)


order.show_cart()
print("\nThank you for ordering! Your food will be delivered soon.")








        




