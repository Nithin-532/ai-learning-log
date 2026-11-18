import math
import numpy as np
import time, random

def dot(a: list[float], b: list[float]) -> float:
    start = time.perf_counter()
    result = sum(x * y for x, y in zip(a, b, strict=True))
    end = time.perf_counter()
    print(end - start)
    return result

def norm(a: list[float]) -> float:
    if len(a) == 0:
        raise ValueError("Vector must not be empty")

    dot_product = dot(a, a)
    return math.sqrt(dot_product)


def cosine_similarity(a: list[float], b: list[float]) -> float:
    norm_a = norm(a)
    norm_b = norm(b)
    if norm_a == 0 or norm_b == 0:
        raise ValueError("Zero vector")

    dot_product = dot(a, b)
    return dot_product / (norm_a * norm_b)

def np_dot(a: list[float], b: list[float]) -> float:
    start = time.perf_counter()
    result = np.dot(a, b)
    end = time.perf_counter()
    print(end - start)
    return result

def np_norm(a: list[float]) -> float:
    return np.linalg.norm(a)

def np_cosine_similarity(a: list[float], b: list[float]) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

a = [random.random() for _ in range(1_000_000)]
b = [random.random() for _ in range(1_000_000)]
a_np, b_np = np.array(a), np.array(b)       # convert ONCE, outside any timer

for label, fn in [
    ("my dot (lists)",   lambda: dot(a, b)),
    ("np.dot (lists)",   lambda: np.dot(a, b)),
    ("np.dot (arrays)",  lambda: np.dot(a_np, b_np)),
]:
    t = time.perf_counter()
    fn()
    print(f"{label:16} {(time.perf_counter() - t) * 1000:.2f} ms")