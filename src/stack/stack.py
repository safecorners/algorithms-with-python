from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class Stack(ABC, Generic[T]):
    @abstractmethod
    def push(self, item: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T | None:
        pass

    @abstractmethod
    def peek(self) -> T | None:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass
