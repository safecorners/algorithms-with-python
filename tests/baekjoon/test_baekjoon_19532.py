from baekjoon.baekjoon_19532 import find_solutions


def test_case_1() -> None:
    actual = find_solutions([1, 3, -1, 4, 1, 7])

    assert actual == [2, -1]


def test_case_2() -> None:
    actual = find_solutions([2, 5, 8, 3, -4, -11])

    assert actual == [-1, 2]
