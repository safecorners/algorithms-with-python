type Matrix = list[list[int]]
type Vector = list[int]


def gcd(a: int, b: int) -> int:
    while True:
        r = a % b
        if r == 0:
            return b
        else:
            a = b
            b = r


def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)


def process(matrix: Matrix) -> Vector:
    """
    [1 0 x]
    [0 1 y]
    """
    row_1 = matrix[0]
    row_2 = matrix[1]

    if row_1[0] == 0:
        row_1, row_2 = row_2, row_1
    # [1 0 x]
    m = abs(lcm(row_1[1], row_2[1]))
    if row_1[1] == m:
        row_1 = [e for e in row_1]
    else:
        row_1 = [e * (m // row_1[1]) for e in row_1]

    if row_2[1] == m:
        row_2 = [e for e in row_2]
    else:
        row_2 = [e * (m // row_2[1]) for e in row_2]

    # row_1 * -1
    row_1 = [e * -1 for e in row_1]

    row_1 = [row_1[i] + row_2[i] for i in range(3)]

    m = abs(gcd(row_1[0], row_1[2]))

    row_1 = [e // m for e in row_1]

    if row_1[0] < 0:
        row_1 = [e * -1 for e in row_1]

    x = row_1[2]

    # [0 1 y]
    if row_2[1] == 0:
        row_1, row_2 = row_2, row_1

    m = abs(lcm(row_1[0], row_2[0]))

    if row_1[0] == m:
        row_1 = [e for e in row_1]
    else:
        row_1 = [e * (m // row_1[0]) for e in row_1]

    if row_2[0] == m:
        row_2 = [e for e in row_2]
    else:
        row_2 = [e * (m // row_2[0]) for e in row_2]

    # row_2 * -1
    row_2 = [e * -1 for e in row_2]

    row_2 = [row_2[i] + row_1[i] for i in range(3)]

    m = abs(gcd(row_2[1], row_2[2]))

    row_2 = [e // m for e in row_2]

    if row_2[1] < 0:
        row_2 = [e * -1 for e in row_2]

    y = row_2[2]
    return [x, y]


if __name__ == "__main__":
    numbers = list(map(int, input().split(" ")))

    matrix = [numbers[:3], numbers[3:]]

    vector = process(matrix)

    print(f"{vector[0]} {vector[1]}")
