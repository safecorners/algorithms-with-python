from baekjoon.p2851 import jump


def test_jump_case_1() -> None:
    input = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    actual = jump(input)

    assert actual == 100


def test_jump_case_2() -> None:
    input = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    actual = jump(input)

    assert actual == 87


def test_jump_case_3() -> None:
    input = [40, 40, 40, 40, 40, 40, 40, 40, 40, 40]

    actual = jump(input)

    assert actual == 120
