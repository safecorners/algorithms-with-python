from typing import List, TypeVar
from sort import SupportsComparion


T = TypeVar("T", bound=SupportsComparion)


def insertion_sort(arr: List[T]) -> None:
    length = len(arr)
    for i in range(length):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
                print(arr)
