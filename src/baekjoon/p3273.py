def find(x: int, n: int, seq: list[int]) -> int:
    count = 0
    start, end = (0, n - 1)

    seq.sort()

    while start < end:
        if seq[start] + seq[end] == x:
            count += 1
            start += 1

        elif seq[start] + seq[end] < x:
            start += 1

        elif seq[start] + seq[end] > x:
            end -= 1

    return count


if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split(" ")))
    x = int(input())

    count = find(x, n, seq)

    print(count)
