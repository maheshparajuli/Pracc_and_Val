def memoize(func):
    cache={}
    def wrapper(*args,**kargs):
        krags_key=tuple(sorted(kargs.items()))

        if (args,krags_key) not in cache:
            cache[(args,krags_key)]=func(*args,**kargs)
        return  cache[(args,krags_key)]
    return wrapper

@memoize
def add(a,b):
    print(a+b)
add(20,43)

