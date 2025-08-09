from baekjoon.p2259 import compute


def test_compute_k_is_2() -> None:
    actual = compute(10, 2, [3, -2, -4, -9, 0, 3, 7, 13, 8, -3])
    assert actual == 21


def test_compute_k_is_5() -> None:
    actual = compute(10, 5, [3, -2, -4, -9, 0, 3, 7, 13, 8, -3])
    assert actual == 31
