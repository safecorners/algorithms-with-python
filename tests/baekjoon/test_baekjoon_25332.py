from baekjoon.baekjoon_25332 import compute


def test_example_1() -> None:
    count = compute(3, [1, 2, 3], [1, 3, 2])
    assert count == 3


def test_example_2() -> None:
    count = compute(5, [1, 2, 3, 4, 5], [14, 5, 6, 7, 8])
    assert count == 0


def test_example_3() -> None:
    count = compute(6, [23, 13, 31, 17, 29, 19], [23, 13, 31, 17, 29, 19])
    assert count == 21


def test_example_4() -> None:
    count = compute(3, [1, 2, 1], [1, 1, 1])
    assert count == 2
