import pytest
from sort.merge_sort import merge_sort


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            [60, 20, 70, 10, 80, 30, 50, 40],
            [10, 20, 30, 40, 50, 60, 70, 80],
        ),
        (
            [20, 15, 35, 45, 40, 10, 30, 25],
            [10, 15, 20, 25, 30, 35, 40, 45],
        ),
        (
            [60, 20, 70, 10, 80, 30, 50, 40, 40, 50],
            [10, 20, 30, 40, 40, 50, 50, 60, 70, 80],
        ),
    ],
)
def test_merge_sort(input: list[int], expected: list[int]) -> None:
    assert merge_sort(input) == expected
