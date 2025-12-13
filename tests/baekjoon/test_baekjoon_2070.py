from baekjoon.baekjoon_2470 import blend


def test_example_1() -> None:
    left, right = blend(5, [-5, 4, -99, -1, 98])
    assert (left, right) == (-99, 98)
