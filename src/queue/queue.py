from __future__ import annotations
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.next: Optional[Node[T]] = None


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.front: Optional[Node[T]] = None
        self.back: Optional[Node[T]] = None

    def enqueue(self, value: T) -> None:
        node = Node(value)
        if self.back is None:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node

    def dequeue(self) -> Optional[T]:
        if self.front is None:
            return None

        value: T = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.back = None

        return value
