""" Just was reading an article about iterators and found out these are the objects where we can use iter() method and next() method.
lets take one simple code:

y="myname"
for x in y:
    print(x)

here in this loop iterator object of y is made and next() method is called.

y="myname"
n=iter(y)
while True:
   try:
        x=next(n)
        print(x)
    except StopIteration:
        break
"""

y="myname"
n=iter(y)
while True:
    try:
        x=next(n)
        print(x)
    except StopIteration:
        print("loop ended")
        break