from __future__ import annotations
from stack.stack import Stack, T
from typing import Generic


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.next: Node[T] | None = None


class LinkedListStack(Stack[T], Generic[T]):
    def __init__(self) -> None:
        self.head: Node[T] | None = None
        self._size = 0

    def push(self, item: T) -> None:
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self) -> T | None:
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return value

    def peek(self) -> T | None:
        if self.head is None:
            return None
        return self.head.value

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        return False

    def size(self) -> int:
        return self._size
