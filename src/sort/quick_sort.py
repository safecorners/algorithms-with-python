from typing import TypeVar, List
from sort import SupportsComparion

T = TypeVar("T", bound=SupportsComparion)


def quick_sort(arr: List[T], left: int = 0, right: int | None = None) -> None:
    if right is None:
        right = len(arr) - 1

    if left < right:
        pivot_index = partition(arr, left, right)

        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)


def partition(arr: List[T], left: int, right: int) -> int:
    pivot_index = left
    left = left + 1

    while left < right:
        while left < len(arr) and arr[left] <= arr[pivot_index]:
            left += 1
        while right > 0 and arr[right] > arr[pivot_index]:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    return right
