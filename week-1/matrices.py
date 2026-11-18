import numpy as np

def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b, strict=True))

def matvec(M: list[list[float]], v: list[float]) -> list[float]:
    return [dot(row, v) for row in M]

print(matvec([[1, 2], [3, 4]], [5, 6]))

