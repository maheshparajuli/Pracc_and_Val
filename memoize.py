from functools import wraps
def memoize(func):
    cache={}
    @wraps(func)
    def wrapper(*args,**kargs):
        krags_key=tuple(sorted(kargs.items()))

        if (args,krags_key) not in cache:
            print("calculating..")
            cache[(args,krags_key)]=func(*args,**kargs)
        return  cache[(args,krags_key)]
    return wrapper

@memoize
def add(a:int,b:int)->int:
    """
    k xa haalchal
    """
    print(a+b)
add(20,43)

add.__wrapped__

# print(add.__name__)
# print(add.__annotations__)
print(add.__doc__)

