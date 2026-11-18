import time
from functools import wraps

def greet():
    return "hi"

say = greet
print(say())
print(say is greet)

def loud(fn):
    def wrapper():
        print("before")
        result = fn()
        print("after")
        return result
    return wrapper

@loud
def bye():
    return "bye"

print(bye())
print(bye.__name__)

greet = loud(greet)
print(greet())

def timer(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{fn.__name__} took {(end_time - start_time) * 1000:.1f} ms")
        return result

    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.2)
    return a + b

print(slow_add(2, 3))
