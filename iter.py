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


y="myname"
n=iter(y)
while True:
    try:
        x=next(n)
        print(x)
    except StopIteration:
        print("loop ended")
        break

class Sequence:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
obj=Sequence()
obj.__iter__()
print(obj.__next__())
print(obj.__next__())

"""
class Sequence:
    def __iter__(self):
        self.a=1
        return self  # returning self.a would give typeerror because it is of type int which is non iterator

    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=x
            # return x
            return x
        else:
            raise StopIteration
see=Sequence()
my=iter(see)

print(next(my))  
print(next(my))    

    



