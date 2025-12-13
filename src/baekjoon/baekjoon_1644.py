from typing import Generator


def multiples() -> Generator[int, None, None]:
    k = 2
    while True:
        yield k
        k += 1


def find_primes(n: int) -> list[int]:
    sieve = [False] + [True] * n

    sieve[1] = False
    for number in range(2, n + 1):
        if sieve[number]:
            for multiple in multiples():
                if number * multiple > n:
                    break
                sieve[number * multiple] = False

    return [number for number in range(2, n + 1) if sieve[number]]


def build_prefix(n: int, primes: list[int]) -> list[int]:
    primes = [0] + primes
    prefix = [0] * len(primes)

    for i in range(1, len(prefix)):
        prefix[i] = prefix[i - 1] + primes[i]

    return prefix


def count_cases(n: int, primes: list[int]) -> int:
    prefix = build_prefix(n, primes)

    count = 0
    start, end = 1, 1

    while end < len(prefix):
        if prefix[end] - prefix[start - 1] < n:
            end += 1
        elif prefix[end] - prefix[start - 1] > n:
            start += 1
        elif prefix[end] - prefix[start - 1] == n:
            count += 1
            end += 1

    return count


if __name__ == "__main__":
    n = int(input())
    primes = find_primes(n)
    count = count_cases(n, primes)
    print(count)
