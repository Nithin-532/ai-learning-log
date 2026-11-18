from contextlib import contextmanager
import time

# class Door:
#     def __enter__(self):
#         print("open")
#         return "inside"

#     def __exit__(self, exc_type, exc, tb):
#         print("close")

# with Door() as where:
#     print(where)
#     raise ValueError("oops")

class Timer:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start_time = time.perf_counter()

    def __exit__(self, exc_type, exc, tb):
        time_taken = (time.perf_counter() - self.start_time) * 1000
        print(f"{self.label} ran for {time_taken:.2f} ms")

@contextmanager
def timer(label):
    start_time = time.perf_counter()
    try:
        yield
    finally:
        time_taken = (time.perf_counter() - start_time) * 1000
        print(f"{label} ran for {time_taken:.2f} ms")

with Timer("sleeping") as t:
    time.sleep(0.2)

with timer("sleeping"):
    time.sleep(0.2)
# prints: sleeping took 200.4 ms