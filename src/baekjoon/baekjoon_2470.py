def blend(n: int, gredients: list[int]) -> tuple[int, int]:
    left = 0
    right = 0
    min_value: int | None = None

    start = 0
    end = n - 1

    gredients.sort()

    while start < end:
        value = gredients[start] + gredients[end]

        if min_value is None:
            min_value = abs(value)
            left = gredients[start]
            right = gredients[end]

        if abs(value) < min_value:
            min_value = abs(value)
            left = gredients[start]
            right = gredients[end]

        if value == 0:
            break
        if value < 0:
            start += 1
        if value > 0:
            end -= 1

    return left, right


if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split(" ")))

    left, right = blend(n, seq)

    print(f"{left} {right}")
