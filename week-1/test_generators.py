import pytest
from generators import chunk_text, batched
from itertools import count, islice
from fake_stream_generator import shout, fake_stream, with_stats
from vectors import dot, norm, cosine_similarity
from toy_semantic import most_similar, add, subtract

@pytest.mark.parametrize(
    "text, size, overlap, expected",
    [
        ("abcdefghij", 4, 1, ["abcd", "defg", "ghij"]),
        ("abcdefghij", 4, 0, ["abcd", "efgh", "ij"]),
        ("abc", 5, 1, ["abc"]),
        ("", 4, 1, []),
    ],
)
def test_chunks(text, size, overlap, expected):
    assert list(chunk_text(text, size, overlap)) == expected


@pytest.mark.parametrize(
    "text, size, overlap, message",
    [
        ("abc", 5, 5, "Overlap must be less than size"),
        ("abc", 0, 1, "Size must be positive"),
        ("abc", 1, -1, "Overlap must be non-negative"),
    ],
)
def test_invalid_args(text, size, overlap, message):
    with pytest.raises(ValueError, match=message):
        chunk_text(text, size, overlap)


@pytest.mark.parametrize(
    "iterable, n, expected",
    [
        (range(7), 3, [[0, 1, 2], [3, 4, 5], [6]]),
        ("abcd", 2, [["a", "b"], ["c", "d"]]),
        ([], 3, []),
    ],
)
def test_batched(iterable, n, expected):
    assert list(batched(iterable, n)) == expected


def test_batched_infinite():
    assert list(islice(batched(count(), 3), 2)) == [[0, 1, 2], [3, 4, 5]]


def test_invalid_batched():
    with pytest.raises(ValueError, match="n must be at least 1"):
        batched("abcd", 0)


def test_shout():
    assert list(shout(["hi", "there"])) == ["HI", "THERE"]


def test_fake_stream():
    assert list(fake_stream("a b c", delay=0)) == ["a", "b", "c"]


def test_empty_stream():
    assert list(with_stats([])) == []


def test_with_stats_reports(capsys):
    assert list(with_stats(["a", "b"])) == ["a", "b"]
    assert "2 pieces" in capsys.readouterr().out


def test_dot():
    assert dot([1, 2, 3], [4, 5, 6]) == 32


def test_norm():
    assert norm([3, 4]) == 5.0


def test_cosine_similarity():
    assert cosine_similarity([1, 0], [0, 1]) == 0.0
    assert cosine_similarity([1, 0], [-1, 0]) == -1.0
    assert cosine_similarity([1, 2], [2, 4]) == pytest.approx(1.0)

def test_mismatched_length_dot_product():
    with pytest.raises(ValueError):
        dot([1, 2, 3], [4, 5])

def test_zero_vector_cosine():
    with pytest.raises(ValueError, match="Zero vector"):
        cosine_similarity([0, 0], [1, 1])

vocab = {
    "king":  [0.9, 0.9, 0.0],
    "queen": [0.9, 0.1, 0.0],
    "man":   [0.1, 0.9, 0.0],
    "woman": [0.1, 0.1, 0.0],
    "apple": [0.0, 0.5, 0.9],
}

def test_most_similar():
    result = most_similar(vocab["apple"], vocab, k=2)
    assert [word for word, _ in result] == ["apple", "man"]
    assert [score for _, score in result] == pytest.approx([1.0, 0.4827], abs=1e-4)

def test_add():
    assert add([1, 2], [3, 4]) == [4, 6]

def test_subtract():
    assert subtract([1, 2], [3, 4]) == [-2, -2]
