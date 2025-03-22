from typing import TypeVar, List
from sort import SupportsComparion

T = TypeVar("T", bound=SupportsComparion)


def quick_sort(arr: List[T], left: int = 0, right: int | None = None) -> None:
    if right is None:
        right = len(arr) - 1

    if left < right:
        pivot = partition(arr, left, right)

        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)


def partition(arr: List[T], left: int, right: int) -> int:
    pivot = left
    left = left + 1

    while True:
        while left < right and arr[left] <= arr[pivot]:
            left += 1
        while right >= left and arr[right] >= arr[pivot]:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[pivot], arr[right] = arr[right], arr[pivot]
            break

    return right
