from baekjoon.baekjoon_2230 import find


def test_length() -> None:
    assert len([1, 5, 3]) == 3


def test_example_one() -> None:
    result = find(3, 3, [1, 5, 3])
    assert result == 4


def test_example_two() -> None:
    result = find(5, 6, [2, 3, 9, 13, 22])

    assert result == 6
