def build_prefix_sum(n: int, sequence: list[int]) -> list[int]:
    sequence = [0] + sequence
    prefix = [0] * len(sequence)

    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + sequence[i]

    return prefix


def count_subsequences_with_sum(n: int, m: int, prefix: list[int]) -> int:
    count = 0
    start, end = 1, 1

    while end <= n:
        if prefix[end] - prefix[start - 1] == m:
            count += 1
            end += 1
        elif prefix[end] - prefix[start - 1] < m:
            end += 1
        else:
            start += 1

    return count


def process(n: int, m: int, sequence: list[int]) -> int:
    prefix = build_prefix_sum(n, sequence)

    count = count_subsequences_with_sum(n, m, prefix)

    return count


if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    sequence = list(map(int, input().split(" ")))

    count = process(n, m, sequence)

    print(count)
