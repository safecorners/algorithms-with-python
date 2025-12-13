from __future__ import annotations


class LinkedListNode[T]:
    def __init__(self, value: T):
        self.value: T = value
        self.next: LinkedListNode[T] | None = None


class LinkedList[T]:
    def __init__(self) -> None:
        self.head: LinkedListNode[T] | None = None
        self.size = 0

    def append(self, value: T) -> None:
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

        self.size += 1

    def lookup(self, index: int) -> LinkedListNode[T] | None:
        current = self.head
        count = 0

        while count < index and current is not None:
            current = current.next
            count += 1
        return current

    def insert(self, index: int, value: T) -> LinkedListNode[T]:
        if index == 0:
            new_head = LinkedListNode(value)
            new_head.next = self.head
            self.head = new_head
            self.size += 1
            return new_head

        current = self.head
        previous: LinkedListNode[T] | None = None
        count = 0
        while count < index and current is not None:
            previous = current
            current = current.next
            count += 1

        if count < index:
            raise IndexError("Index out of bounds")

        new_node = LinkedListNode(value)
        if previous is not None:
            new_node.next = previous.next
            previous.next = new_node

        self.size += 1
        return new_node

    def remove(self, index: int) -> LinkedListNode[T] | None:
        if self.head is None:
            return None

        if index == 0:
            new_head = self.head.next
            self.head.next = None
            self.head = new_head
            self.size -= 1
            return new_head

        current: LinkedListNode[T] | None = self.head
        previous: LinkedListNode[T] | None = None
        count = 0
        while count < index and current is not None:
            previous = current
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Index out of bounds")

        if previous is None:
            return None

        previous.next = current.next
        current.next = None
        self.size -= 1
        return current

    def __len__(self) -> int:
        return self.size
