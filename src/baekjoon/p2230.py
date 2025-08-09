def find(n: int, m: int, sequence: list[int]) -> int:
    sequence.sort()

    minimum: int | None = None

    end = 0
    for start in range(n):
        while end < n and sequence[end] - sequence[start] < m:
            end += 1

        if end == n:
            break

        value = sequence[end] - sequence[start]
        if value >= m and (minimum is None or minimum >= value):
            minimum = value

    assert minimum is not None
    return minimum


if __name__ == "__main__":
    n, m = map(int, input().split(" "))

    sequence = [int(input()) for _ in range(n)]

    result = find(n, m, sequence)

    print(result)
