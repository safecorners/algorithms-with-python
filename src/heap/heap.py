from abc import ABC, abstractmethod
from typing import Protocol, Self, TypeVar


class SupportsComparable(Protocol):
    def __le__(self, other: Self) -> bool: ...
    def __lt__(self, other: Self) -> bool: ...
    def __ge__(self, other: Self) -> bool: ...
    def __gt__(self, other: Self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...


T = TypeVar("T", bound=SupportsComparable)


class Heap[T](ABC):
    @abstractmethod
    def insert(self, value: T) -> None:
        raise NotImplementedError()

    @abstractmethod
    def remove(self) -> T | None:
        raise NotImplementedError()
