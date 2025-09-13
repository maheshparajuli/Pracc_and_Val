def run(func):
    def wrapper():
        for i in range(3):
            func()
    return wrapper

@run
def greet():
    print("mam khayeu?, Dashain aaudai xa, Mashu pani Khayeu hola?")
greet()