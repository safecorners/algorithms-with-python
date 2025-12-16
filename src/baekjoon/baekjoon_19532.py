def find_solutions(numbers: list[int]) -> list[int]:
    a, b, c, d, e, f = numbers
    for x in range(-999, 999 + 1):
        for y in range(-999, 999 + 1):
            if a * x + b * y == c and d * x + e * y == f:
                return [x, y]

    raise ValueError


if __name__ == "__main__":
    numbers = list(map(int, input().split(" ")))

    results = find_solutions(numbers)

    print(*results)
