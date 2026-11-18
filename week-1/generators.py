from collections.abc import Iterator
from itertools import count, islice


def _iter_batches(it, n: int):
    batch = []
    for i in it:
        batch.append(i)
        if len(batch) == n:
            yield batch
            batch = []

    if batch:
        yield batch


def batched(iterable, n: int):
    """Yield lists of n items; the last batch may be shorter."""
    if n < 1:
        raise ValueError("n must be at least 1")

    new_iterable = iter(iterable)

    return _iter_batches(new_iterable, n)


def _iter_chunks(text: str, size: int, overlap: int):
    for i in range(0, len(text), size - overlap):
        yield text[i : i + size]
        if i + size >= len(text):
            break


def chunk_text(text: str, size: int, overlap: int) -> Iterator[str]:
    """Yield chunks of `size` chars, each overlapping the previous by `overlap` chars."""
    if size <= 0:
        raise ValueError("Size must be positive")
    if overlap >= size:
        raise ValueError("Overlap must be less than size")
    if overlap < 0:
        raise ValueError("Overlap must be non-negative")

    return _iter_chunks(text, size, overlap)


# print(list(chunk_text("abcdefghij", 4, 1)))
# print(list(chunk_text("abcdefghij", 4, 0)))
# print(list(chunk_text("abc", 5, 1)))
# print(list(chunk_text("", 4, 1)))
# chunk_text("abc", 5, 5)

print(list(batched(range(7), 3)))
print(list(batched("abcd", 2)))
print(list(batched([], 3)))
print(list(islice(batched(count(), 3), 2)))
