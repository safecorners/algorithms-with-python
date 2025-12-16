from typing import Tuple, List, Optional

Point = Tuple[int, int]


def calculate_distances(x: int, y: int, points: List[Point]) -> List[int]:
    return sorted([abs(x - px) + abs(y - py) for px, py in points])


def accumulate_distances(distances: List[int]) -> List[int]:
    running_sum = 0
    accumulated = []
    for distance in distances:
        running_sum += distance
        accumulated.append(running_sum)

    return accumulated


def is_better_distance(current: Optional[int], new: int) -> bool:
    return current is None or new < current


def minimize_distances(n: int, points: List[Point]) -> List[int]:
    xs = [x for (x, _) in points]
    ys = [y for (_, y) in points]
    min_dists: List[Optional[int]] = [None] * n

    for x in xs:
        for y in ys:
            dists = calculate_distances(x, y, points)
            acc_dists: List[int] = accumulate_distances(dists)

            for i in range(n):
                if is_better_distance(min_dists[i], acc_dists[i]):
                    min_dists[i] = acc_dists[i]

    return [dist if dist is not None else 0 for dist in min_dists]


if __name__ == "__main__":
    n = int(input())
    points: List[Point] = []
    for _ in range(n):
        px, py = tuple(map(int, input().split(" ")))
        points.append((px, py))

    distances = minimize_distances(n, points)

    print(*distances)
