import time

def timer(func):
    def wrapper(*args,**kargs):
        t_start=time.time()
        result=func(*args,**kargs)
        t_total=time.time()-t_start
        print("{} took {} seconds".format(func.__name__,t_total))
        return result
    return wrapper

@timer
def add(a,b):
    print(a+b)
add(1,2)
    
