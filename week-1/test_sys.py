import sys

print(sys.getsizeof([x * x for x in range(1_000_000)]))
print(sys.getsizeof((x * x for x in range(1_000_000))))
print(sys.getsizeof((x * x for x in range(10**9))))
