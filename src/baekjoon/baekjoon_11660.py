from dataclasses import dataclass


type Matrix = list[list[int]]


@dataclass
class Point:
    i: int
    j: int


def compute_prefix(n: int, mat: Matrix) -> Matrix:
    p = n + 1

    mat = [[0] * p] + [[0] + mat[i] for i in range(n)]

    prefix = [[0] * p for _ in range(p)]
    for i in range(1, p):
        for j in range(1, p):
            prefix[i][j] = (
                mat[i][j] + prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1]
            )

    return prefix


def compute_range_sum(start: Point, end: Point, prefix: Matrix) -> int:
    return (
        prefix[end.i][end.j]
        - prefix[start.i - 1][end.j]
        - prefix[end.i][start.j - 1]
        + prefix[start.i - 1][start.j - 1]
    )


def compute(
    n: int, m: int, arr: Matrix, ranges: list[tuple[Point, Point]]
) -> list[int]:
    prefix = compute_prefix(n, arr)
    results: list[int] = []
    for start, end in ranges:
        range_sum = compute_range_sum(start, end, prefix)
        results.append(range_sum)

    return results


if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    mat = [list(map(int, input().split(" "))) for _ in range(n)]
    ranges = [
        (Point(a, b), Point(c, d))
        for a, b, c, d in [map(int, input().split(" ")) for _ in range(m)]
    ]

    results = compute(n, m, mat, ranges)
    for result in results:
        print(result)
