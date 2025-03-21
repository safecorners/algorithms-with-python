from typing import List, TypeVar
from sort import SupportsComparion


T = TypeVar("T", bound=SupportsComparion)


def selection_sort(arr: List[T]) -> None:
    length = len(arr)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j

        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
