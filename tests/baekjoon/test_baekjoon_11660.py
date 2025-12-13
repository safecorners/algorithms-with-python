import pytest

from baekjoon.baekjoon_11660 import compute, Point, Matrix


@pytest.fixture
def matrix_1() -> Matrix:
    return [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6],
        [4, 5, 6, 7],
    ]


def test_example_one(matrix_1: Matrix) -> None:
    results = compute(
        4,
        3,
        matrix_1,
        [
            (Point(2, 2), Point(3, 4)),
            (Point(3, 4), Point(3, 4)),
            (Point(1, 1), Point(4, 4)),
        ],
    )
    assert results == [27, 6, 64]


def test_example_two() -> None:
    results = compute(
        2,
        4,
        [
            [1, 2],
            [3, 4],
        ],
        [
            (Point(1, 1), Point(1, 1)),
            (Point(1, 2), Point(1, 2)),
            (Point(2, 1), Point(2, 1)),
            (Point(2, 2), Point(2, 2)),
        ],
    )

    assert results == [1, 2, 3, 4]
