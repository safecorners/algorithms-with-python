from stack.stack import Stack, T
from typing import Generic


class ArrayStack(Stack[T], Generic[T]):
    def __init__(self, capacity: int = 10) -> None:
        self._capacity = capacity
        self.items: list[T | None] = [None] * capacity
        self._size = 0

    def push(self, item: T) -> None:
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self.items[self._size] = item
        self._size += 1

    def pop(self) -> T | None:
        if self.is_empty():
            return None
        self._size -= 1
        item = self.items[self._size]
        self.items[self._size] = None
        return item

    def peek(self) -> T | None:
        if self.is_empty():
            return None
        return self.items[self._size - 1]

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def _resize(self, new_capacity: int) -> None:
        self._capacity = new_capacity
        new_items: list[T | None] = [None] * new_capacity
        for i in range(self._size):
            new_items[i] = self.items[i]
        self.items = new_items
