from baekjoon.baekjoon_7696 import compute


def test_compute_single_digit() -> None:
    actual = compute(9)

    assert actual == 9


def test_compute_double_digit() -> None:
    actual = compute(25)

    assert actual == 27
