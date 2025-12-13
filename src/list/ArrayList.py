from typing import Generic, TypeVar

T = TypeVar("T")


class ArrayList(Generic[T]):
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.items: list[T | None] = [None] * capacity
        self.size = 0

    def add(self, item: T) -> None:
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.items[self.size] = item
        self.size += 1

    def resize(self, new_capacity: int) -> None:
        raise NotImplementedError("Resize method not implemented")
