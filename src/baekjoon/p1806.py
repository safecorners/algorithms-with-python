def find_shortest_length(s: int, n: int, sequence: list[int]) -> int:
    sequence = [0] + sequence

    prefix = [0] * len(sequence)

    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + sequence[i]

    start = 1
    end = 1
    shortest = n + 1
    while start <= end and end < n + 1:
        value = prefix[end] - prefix[start - 1]

        if value < s:
            end += 1
        elif value >= s:
            if shortest > end - start + 1:
                shortest = end - start + 1
            start += 1

    if shortest == n + 1:
        shortest = 0
    return shortest


if __name__ == "__main__":
    n, s = map(int, input().split(" "))
    sequence = list(map(int, input().split(" ")))

    shortest = find_shortest_length(s=s, n=n, sequence=sequence)

    print(shortest)
