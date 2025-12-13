from baekjoon.baekjoon_15652 import non_dec_seq


def test_example_one() -> None:
    assert non_dec_seq(3, 1) == [[1], [2], [3]]


def test_example_two() -> None:
    expect = [
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 2],
        [2, 3],
        [2, 4],
        [3, 3],
        [3, 4],
        [4, 4],
    ]

    assert non_dec_seq(4, 2) == expect


def test_example_three() -> None:
    expect = [
        [1, 1, 1],
        [1, 1, 2],
        [1, 1, 3],
        [1, 2, 2],
        [1, 2, 3],
        [1, 3, 3],
        [2, 2, 2],
        [2, 2, 3],
        [2, 3, 3],
        [3, 3, 3],
    ]

    assert non_dec_seq(3, 3) == expect
