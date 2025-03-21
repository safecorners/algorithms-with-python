from typing import List, TypeVar
from sort import SupportsComparion

T = TypeVar("T", bound=SupportsComparion)


def merge_sort(arr: List[T]) -> List[T]:
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def merge(left: List[T], right: List[T]) -> List[T]:
    i = j = 0
    result: List[T] = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    for i in range(i, len(left)):
        result.append(left[i])
    for j in range(j, len(right)):
        result.append(right[j])

    return result
