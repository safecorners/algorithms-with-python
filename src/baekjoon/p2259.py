def compute(n: int, k: int, arr: list[int]) -> int:
    arr = [0] + arr
    prefix = [0] * len(arr)

    # Compute prefix
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    # Compute sum
    sum = [0] * len(arr)
    for i in range(k, n + 1):
        sum[i] = prefix[i] - prefix[i - k]

    # Find max
    max = None
    for i in range(k, n + 1):
        if max is None:
            max = sum[i]
        if max < sum[i]:
            max = sum[i]

    assert max is not None
    return max


if __name__ == "__main__":
    n, k = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    max = compute(n, k, arr)
    print(max)
