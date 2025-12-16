from baekjoon.baekjoon_1090 import minimize_distances


def test_example_1() -> None:
    assert [0, 2, 3, 4] == minimize_distances(
        4, [(15, 14), (15, 16), (14, 15), (16, 15)]
    )


def test_example_2() -> None:
    assert [0, 1, 3, 10] == minimize_distances(4, [(1, 1), (2, 1), (4, 1), (9, 1)])


def test_example_3() -> None:
    assert [0, 0] == minimize_distances(2, [(4, 7), (4, 7)])
