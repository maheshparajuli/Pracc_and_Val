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

"""Lets try something good.
I will create problem by myself.
Q. Create one form that takes input about username, account name and one can access account money after entering account name and username.
 """



"""multiple inheritance: taking features from many classes, two or more than two.
.get(key, default) is a dictionary method that tries to fetch the value for the given key.
"""

class Person:
    def __init__(self):
        


        




