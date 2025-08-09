from baekjoon.p3273 import find


def test_example_1() -> None:
    count = find(13, 9, [5, 12, 7, 10, 9, 1, 2, 3, 11])

    assert count == 3
