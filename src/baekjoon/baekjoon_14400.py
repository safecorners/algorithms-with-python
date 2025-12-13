class Box:
    def __init__(
        self,
        x_beginning: int,
        y_beginning: int,
        x_end: int,
        y_end: int,
    ):
        self.x_beginning = x_beginning
        self.y_beginning = y_beginning
        self.x_end = x_end
        self.y_end = y_end

    def area(self) -> int:
        return (self.x_end - self.x_beginning) * (self.y_end - self.y_beginning)


def intersection(box_1: Box, box_2: Box) -> Box:
    # Case 1: Box2 intersect right over
    if (
        (box_1.x_beginning <= box_2.x_beginning)
        and (box_2.x_beginning <= box_1.x_end)
        and (box_1.y_beginning <= box_2.y_beginning)
        and (box_2.y_beginning <= box_1.y_end)
    ):
        return Box(
            box_2.x_beginning,
            box_2.y_beginning,
            box_1.x_end,
            box_1.y_end,
        )

    # Case 2: Box2 intersect left over
    if (
        (box_2.x_beginning <= box_1.x_beginning)
        and (box_1.x_beginning <= box_2.x_end)
        and (box_1.y_beginning <= box_2.y_beginning)
        and (box_2.y_beginning <= box_1.y_end)
    ):
        return Box(
            box_1.x_beginning,
            box_2.y_beginning,
            box_2.x_end,
            box_1.y_end,
        )

    # Case 3: Box2 intersect left under
    if (
        (box_2.x_beginning <= box_1.x_beginning)
        and (box_1.x_beginning <= box_2.x_end)
        and (box_1.y_beginning <= box_2.y_end)
        and (box_2.y_end <= box_1.y_end)
    ):
        return Box(
            box_1.x_beginning,
            box_1.y_beginning,
            box_2.x_end,
            box_2.y_end,
        )

    # Right Over Overlap
    if (
        (box_1.x_beginning <= box_2.x_beginning)
        and (box_2.x_beginning <= box_1.x_end)
        and (box_1.y_beginning <= box_2.y_end)
        and (box_2.y_end <= box_1.y_end)
    ):
        return Box(
            box_2.x_beginning,
            box_1.y_beginning,
            box_1.x_end,
            box_2.y_end,
        )

    return Box(0, 0, 0, 0)


def calc(boxes: list[Box]) -> list[list[int]]:
    n = boxes.__len__()
    result = []

    for i in range(n):
        for j in range(i):
            result.append([i, j])

    return result
