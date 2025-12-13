from baekjoon.baekjoon_2015 import compute


def test_example_1() -> None:
    assert compute(4, 0, [2, -2, 2, -2]) == 4


def test_example_2() -> None:
    assert compute(6, 5, [1, 2, 3, 4, 5, 0]) == 3
