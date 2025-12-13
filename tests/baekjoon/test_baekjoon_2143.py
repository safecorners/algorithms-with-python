from baekjoon.baekjoon_2143 import compute


def test_example_1() -> None:
    count = compute(5, 4, [1, 3, 1, 2], 3, [1, 3, 2])
    assert count == 7


def test_subset() -> None:
    count = compute(2, 1, [1], 1, [1])
    assert count == 1
