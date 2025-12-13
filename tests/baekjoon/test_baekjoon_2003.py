from baekjoon.baekjoon_2003 import build_prefix_sum, process


def test_prefix_sum() -> None:
    prefix = build_prefix_sum(4, [1, 1, 1, 1])
    assert prefix == [0, 1, 2, 3, 4]


def test_prefix_sum_with_example_two() -> None:
    prefix = build_prefix_sum(10, [1, 2, 3, 4, 2, 5, 3, 1, 1, 2])
    assert prefix == [0, 1, 3, 6, 10, 12, 17, 20, 21, 22, 24]


def test_example_one() -> None:
    count = process(4, 2, [1, 1, 1, 1])

    assert count == 3


def test_example_two() -> None:
    count = process(10, 5, [1, 2, 3, 4, 2, 5, 3, 1, 1, 2])

    assert count == 3
