from baekjoon.baekjoon_15961 import maximize_combinations


def test_concatenation() -> None:
    seq = [7, 9, 7, 30, 2, 7, 9, 25]

    seq = seq[:] + seq[0:3]

    assert seq == [7, 9, 7, 30, 2, 7, 9, 25, 7, 9, 7]


def test_slice() -> None:
    seq = [7, 9, 7, 30, 2, 7, 9, 25]

    assert seq[0:3] == [7, 9, 7]


def test_example_one() -> None:
    count = maximize_combinations(8, 30, 4, 30, [7, 9, 7, 30, 2, 7, 9, 25])
    assert count == 5


def test_example_two() -> None:
    count = maximize_combinations(8, 50, 4, 7, [2, 7, 9, 25, 7, 9, 7, 30])
    assert count == 4
