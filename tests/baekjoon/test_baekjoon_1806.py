from baekjoon.baekjoon_1806 import find_shortest_length


def test_example_1() -> None:
    shortest = find_shortest_length(15, 10, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8])

    assert shortest == 2


def test_example_2() -> None:
    shortest = find_shortest_length(15, 5, [5, 1, 3, 5, 10])
    assert shortest == 2
