import time


def fake_stream(text: str, delay: float = 0.1):
    """Yield one word at a time, sleeping `delay` seconds before each."""
    for word in text.split():
        time.sleep(delay)
        yield word
    word = ""


def shout(stream):
    """Wrap any iterable of strings; yield each piece uppercased."""
    for word in stream:
        yield word.upper()


def with_stats(stream):
    """Pass every piece through unchanged. When the stream ends, print
    the number of pieces and the time-to-first-token (TTFT) in ms."""
    ttft_ms = None
    total_pieces = 0

    try:
        start = time.perf_counter()
        for piece in stream:
            if ttft_ms is None:
                end = time.perf_counter()
                ttft_ms = (end - start) * 1000
            total_pieces += 1
            yield piece

    finally:
        ttft = f"{ttft_ms:.1f} ms" if ttft_ms is not None else "n/a"
        print(f"\n{total_pieces} pieces, TTFT {ttft}")


if __name__ == "__main__":
    for piece in with_stats(shout(fake_stream("the quick brown fox jumps"))):
        print(piece, end=" ", flush=True)

    # for i, piece in enumerate(with_stats(shout(fake_stream("the quick brown fox jumps")))):
    #     print(piece, end=" ", flush=True)
    #     if i == 1:
    #         break
