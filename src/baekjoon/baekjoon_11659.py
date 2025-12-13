def compute_prefix_sum(arr: list[int]) -> list[int]:
    arr = [0] + arr
    prefix = [0] * len(arr)

    for i in range(len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    ranges: list[tuple[int, int]] = []
    for _ in range(m):
        i, j = map(int, input().split(" "))
        ranges.append((i, j))

    prefix = compute_prefix_sum(arr)

    for i, j in ranges:
        print(prefix[j] - prefix[i - 1])
