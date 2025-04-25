from __future__ import annotations

from typing import Protocol, TypeVar, Any


class SupportsComparion(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...


T = TypeVar("T", bound=SupportsComparion)


def iterative_binary_search(arr: list[T], target: T) -> T | None:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return arr[mid]

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None
