from baekjoon.baekjoon_19532 import gcd, lcm, process


def test_gcd() -> None:
    assert gcd(24, 18) == 6


def test_lcm() -> None:
    assert lcm(24, 18) == 72

    assert lcm(3, 1) == 3


def test_case_one() -> None:
    actual = process([[1, 3, -1], [4, 1, 7]])

    assert actual == [2, -1]


def test_case_two() -> None:
    actual = process([[2, 5, 8], [3, -4, -11]])

    assert actual == [-1, 2]
