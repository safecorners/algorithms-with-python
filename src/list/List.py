from abc import ABC, abstractmethod


class List[T](ABC):
    @abstractmethod
    def append(self, item: T) -> None:
        raise NotImplementedError()

    @abstractmethod
    def remove(self, item: T) -> None:
        raise NotImplementedError()
