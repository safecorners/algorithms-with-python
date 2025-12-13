from baekjoon.baekjoon_15650 import combination


def test_3C1() -> None:
    assert combination(3, 1) == [[1], [2], [3]]


def test_4C2() -> None:
    actual = combination(4, 2)

    expect = [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4],
    ]

    assert actual == expect


def test_4C4() -> None:
    assert combination(4, 4) == [[1, 2, 3, 4]]
