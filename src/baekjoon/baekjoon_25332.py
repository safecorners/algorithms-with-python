def compute(n: int, a: list[int], b: list[int]) -> int:
    """
    1. count when a[i:j] == b[i:j], it means
    2. prefix[a][j] - prefix[a][i] == prefix[b][j] - prefix[b][i], to transpose
    3. prefix[a][j] - prefix[b][j] == prefix[a][i] - prefix[b][i]
    """
    length = n + 1

    prefix = {
        "a": [0] * length,
        "b": [0] * length,
    }

    seq = {
        "a": [0] + a,
        "b": [0] + b,
    }

    for i in range(1, length):
        prefix["a"][i] = prefix["a"][i - 1] + seq["a"][i]
        prefix["b"][i] = prefix["b"][i - 1] + seq["b"][i]

    count = 0
    diff_counts: dict[int, int] = {}
    for i in range(1, length):
        if prefix["a"][i] == prefix["b"][i]:
            count = count + 1

        difference = prefix["a"][i] - prefix["b"][i]
        count = count + diff_counts.get(difference, 0)

        if difference in diff_counts:
            diff_counts[difference] = diff_counts[difference] + 1
        else:
            diff_counts[difference] = 1

    return count


if __name__ == "__main__":
    n = int(input())

    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))

    count = compute(n, a, b)

    print(count)
