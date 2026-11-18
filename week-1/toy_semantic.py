import numpy as np
from vectors import np_cosine_similarity 

vocab = {
    "king":  [0.9, 0.9, 0.0],
    "queen": [0.9, 0.1, 0.0],
    "man":   [0.1, 0.9, 0.0],
    "woman": [0.1, 0.1, 0.0],
    "apple": [0.0, 0.5, 0.9],
}

def most_similar(query: list[float], vocab: dict[str, list[float]], k: int = 3) -> list[tuple[str, float]]:
    scores = [(word, np_cosine_similarity(np.array(query), np.array(vec))) for word, vec in vocab.items()]
    sorted_data = sorted(scores, key=lambda item: item[1], reverse=True)
    return sorted_data[:k]

def add(a: list[float], b: list[float]) -> list[float]:
    return [x + y for x, y in zip(a, b, strict=True)]

def subtract(a: list[float], b: list[float]) -> list[float]:
    return [x - y for x, y in zip(a, b, strict=True)]

for top_vocab, score in most_similar(vocab["apple"], vocab, k=2):
    print(f"{top_vocab} {score:.2f}")
print(most_similar(vocab["queen"], vocab, k=len(vocab)))
print(add([1, 2], [3, 4]))        # → [4, 6]
print(subtract([1, 2], [3, 4]))   # → [-2, -2]
result = add(subtract(vocab["king"], vocab["man"]), vocab["woman"])
print(result)                          # ≈ [0.9, 0.1, 0.0]  (tiny float noise is possible; you know why now)
print(most_similar(result, vocab, k=1))