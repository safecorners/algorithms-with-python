def compute(n: int, k: int, sequence: list[int]) -> int:
    sequence = [0] + sequence
    prefix = [0] * len(sequence)

    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + sequence[i]

    count = 0
    prefix_sum_counts: dict[int, int] = {}

    for i in range(1, n + 1):
        if prefix[i] == k:
            count += 1
        count += prefix_sum_counts.get(prefix[i], 0)

        if prefix[i] + k in prefix_sum_counts:
            prefix_sum_counts[prefix[i] + k] += 1
        else:
            prefix_sum_counts[prefix[i] + k] = 1

    return count


if __name__ == "__main__":
    n, k = map(int, input().split(" "))
    seq = list(map(int, input().split(" ")))

    result = compute(n, k, seq)
    print(result)
