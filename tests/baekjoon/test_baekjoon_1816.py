from baekjoon.baekjoon_1816 import find_primes, is_valid


def test_find_primes() -> None:
    assert find_primes(17) == [2, 3, 5, 7, 11, 13, 17]
    assert find_primes(16) == [2, 3, 5, 7, 11, 13]
    assert find_primes(18) == [2, 3, 5, 7, 11, 13, 17]


def test_is_valid() -> None:
    primes = find_primes(int(10**6))

    assert is_valid(1000036000099, primes) is True
    assert is_valid(1500035500153, primes) is False
    assert is_valid(20000000000002, primes) is False
