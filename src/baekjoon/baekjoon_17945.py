import math


def solve(a: int, b: int) -> tuple[int, int]:
    left = -1 * a
    right = math.sqrt((a * a) - b)
    x_1 = left + right
    x_2 = left - right

    return (int(x_1), int(x_2))


if __name__ == "__main__":
    a, b = map(int, input().split(" "))

    x_1, x_2 = solve(a, b)

    if x_1 == x_2:
        print(x_1)
    else:
        if x_1 > x_2:
            print(f"{x_2} {x_1}")
        else:
            print(f"{x_1} {x_2}")
