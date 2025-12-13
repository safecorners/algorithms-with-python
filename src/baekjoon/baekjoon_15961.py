import sys

input = sys.stdin.readline


def maximize_combinations(n: int, d: int, k: int, c: int, dishes: list[int]) -> int:
    dishes = dishes[:] + dishes[0:k]

    sushis: dict[int, int] = {}
    sushis[c] = 1
    for i in range(0, k):
        sushi = dishes[i]
        if sushi in sushis:
            sushis[sushi] += 1
        else:
            sushis[sushi] = 1
    count = 0
    for sushi in sushis:
        count += 1

    maximum = count
    start, end = 0, k - 1
    while end < n + k - 1:
        start, end = start + 1, end + 1

        sushis[dishes[start - 1]] -= 1
        if sushis[dishes[start - 1]] == 0:
            count -= 1
            del sushis[dishes[start - 1]]

        if dishes[end] in sushis:
            sushis[dishes[end]] += 1
        else:
            sushis[dishes[end]] = 1
            count += 1

        if count > maximum:
            maximum = count

    return maximum


if __name__ == "__main__":
    n, d, k, c = list(map(int, input().split(" ")))
    dishes = [int(input()) for _ in range(1, n + 1)]

    maximum = maximize_combinations(n, d, k, c, dishes)

    print(maximum)
