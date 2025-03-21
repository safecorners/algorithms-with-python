from typing import TypeVar, List
from sort import SupportsComparion


T = TypeVar("T", bound=SupportsComparion)


def bubble_sort(arr: List[T]) -> None:
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
