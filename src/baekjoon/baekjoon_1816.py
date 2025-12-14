import math
import sys

input = sys.stdin.readline


def find_primes(m: int) -> list[int]:
    primes = [False] + [True] * m

    primes[1] = False
    for i in range(2, int(math.sqrt(m)) + 1):
        if primes[i]:
            for j in range(i * i, m + 1, i):
                primes[j] = False

    return [x for x in range(2, m + 1) if primes[x]]


def is_valid(key: int, primes: list[int]) -> bool:
    for prime in primes:
        if key % prime == 0:
            return False
        if prime * prime > key:
            break

    return True


if __name__ == "__main__":
    n = int(input())
    keys = [int(input()) for _ in range(n)]

    m = int(10**6)
    primes = find_primes(m)

    results = [is_valid(key, primes) for key in keys]

    for result in results:
        if result:
            print("YES")
        else:
            print("NO")
