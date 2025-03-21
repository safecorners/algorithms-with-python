import pytest
from typing import List
from sort.quick_sort import quick_sort
from sort.quick_sort import partition


@pytest.mark.parametrize(
    "arr, expected",
    [
        (
            [30, 45, 20, 15, 40, 25, 35, 10],
            [10, 15, 20, 25, 30, 35, 40, 45],
        ),
        (
            [30, 45, 20, 15, 40, 25, 35, 10, 30, 25],
            [10, 15, 20, 25, 25, 30, 30, 35, 40, 45],
        ),
        (
            [30, 50, 17, 40, 88, 15, 44, 55, 22, 11, 66, 13, 85],
            [11, 13, 15, 17, 22, 30, 40, 44, 50, 55, 66, 85, 88],
        ),
    ],
)
def test_quick_sort(arr: List[int], expected: List[int]) -> None:
    quick_sort(arr)
    assert arr == expected


@pytest.mark.parametrize(
    "arr",
    [
        ([2, 2, 2, 2]),
        ([2, 2, 2, 2, 2]),
    ],
)
def test_partition_multiple_values_equals_pivot(arr: List[int]) -> None:
    actual = partition(arr, 0, len(arr) - 1)
    expected = len(arr) // 2 if len(arr) % 2 == 0 else len(arr) // 2 + 1
    assert actual == expected
