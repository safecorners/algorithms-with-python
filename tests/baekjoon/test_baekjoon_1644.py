from baekjoon.baekjoon_1644 import find_primes, count_cases, build_prefix


def test_find_primes() -> None:
    primes = find_primes(41)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]


def test_build_prefix() -> None:
    prefix = build_prefix(17, find_primes(17))
    assert prefix == [0, 2, 5, 10, 17, 28, 41, 58]


def test_example_one() -> None:
    assert count_cases(20, find_primes(20)) == 0


def test_example_two() -> None:
    assert count_cases(3, find_primes(3)) == 1


def test_example_three() -> None:
    assert count_cases(41, find_primes(41)) == 3


def test_example_4() -> None:
    assert count_cases(53, find_primes(53)) == 2
