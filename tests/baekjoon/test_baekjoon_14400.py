from baekjoon.baekjoon_14400 import Box, intersection, calc


def test_left_over() -> None:
    box_1 = Box(3, 7, 3 + 10, 7 + 10)
    box_2 = Box(5, 2, 5 + 10, 2 + 10)

    result = intersection(box_1, box_2)

    assert result.area() == 40


def test_right_under() -> None:
    box_2 = Box(3, 7, 3 + 10, 7 + 10)
    box_1 = Box(5, 2, 5 + 10, 2 + 10)

    result = intersection(box_1, box_2)

    assert result.area() == 40


def test_not_overlapping() -> None:
    box_1 = Box(3, 7, 3 + 10, 7 + 10)
    box_2 = Box(5, 2, 5 + 10, 2 + 10)
    box_3 = Box(15, 7, 15 + 10, 7 + 10)

    actual = intersection(box_1, box_3)
    assert actual.area() == 0

    actual = intersection(box_2, box_3)
    assert actual.area() == 0


def test_sum() -> None:
    boxes = [
        Box(3, 7, 3 + 10, 7 + 10),
        Box(5, 2, 5 + 10, 2 + 10),
        Box(15, 7, 15 + 10, 7 + 10),
    ]

    print(f"result = {calc(boxes)}")
