from heap.heap import Heap, T


class MaxHeap(Heap[T]):
    def __init__(self) -> None:
        self.list: list[T] = []
        self.size = 0

    def insert(self, value: T) -> None:
        index = 1
        left = index * 2
        right = index * 2 + 1

        while True:
            if self.list[index] is None:
                self.list[index] = value
                self.size += 1
                return
            if self.list[index] > value:
                if self.list[left] is None:
                    index = left
                if self.list[right] is None:
                    index = right

    def remove(self) -> T | None:
        if self.size == 0:
            return None

        raise NotImplementedError()
