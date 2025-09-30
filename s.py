import datetime
import time

# Decorator to log execution time
def log_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        print(f"[START] {func.__name__} at {start.strftime('%Y-%m-%d %H:%M:%S')}")

        result = func(*args, **kwargs)

        end = datetime.datetime.now()
        duration = (end - start).total_seconds()
        print(f"[END] {func.__name__} at {end.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"[DURATION] {func.__name__} took {duration:.2f} seconds\n")
        return result
    return wrapper

# Example functions using the decorator
@log_time
def slow_task():
    print("Running slow task...")
    time.sleep(2)

@log_time
def fast_task():
    print("Running fast task...")
    time.sleep(0.5)

# Run them
slow_task()
fast_task()
