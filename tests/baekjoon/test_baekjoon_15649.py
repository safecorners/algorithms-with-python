from baekjoon.baekjoon_15649 import permutation


def test_3P1() -> None:
    actual = permutation(3, 1)

    assert actual == [[1], [2], [3]]


def test_4P2() -> None:
    actual = permutation(4, 2)

    expect = [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 1],
        [2, 3],
        [2, 4],
        [3, 1],
        [3, 2],
        [3, 4],
        [4, 1],
        [4, 2],
        [4, 3],
    ]

    assert actual == expect


def test_example_4P4() -> None:
    actual = permutation(4, 4)

    expect = [
        [1, 2, 3, 4],
        [1, 2, 4, 3],
        [1, 3, 2, 4],
        [1, 3, 4, 2],
        [1, 4, 2, 3],
        [1, 4, 3, 2],
        [2, 1, 3, 4],
        [2, 1, 4, 3],
        [2, 3, 1, 4],
        [2, 3, 4, 1],
        [2, 4, 1, 3],
        [2, 4, 3, 1],
        [3, 1, 2, 4],
        [3, 1, 4, 2],
        [3, 2, 1, 4],
        [3, 2, 4, 1],
        [3, 4, 1, 2],
        [3, 4, 2, 1],
        [4, 1, 2, 3],
        [4, 1, 3, 2],
        [4, 2, 1, 3],
        [4, 2, 3, 1],
        [4, 3, 1, 2],
        [4, 3, 2, 1],
    ]

    assert actual == expect
