from __future__ import annotations
from typing import TypeVar, Generic, Protocol, Self


class SupportsComparable(Protocol):
    def __lt__(self, other: Self) -> bool: ...
    def __le__(self, other: Self) -> bool: ...
    def __ge__(self, other: Self) -> bool: ...
    def __gt__(self, other: Self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...


T = TypeVar("T", bound=SupportsComparable)


class TreeNode(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.left: TreeNode[T] | None = None
        self.right: TreeNode[T] | None = None
        self.parent: TreeNode[T] | None = None


class BinarySearchTree(Generic[T]):
    def __init__(self) -> None:
        self.root: TreeNode[T] | None = None

    def insert(self, value: T) -> None:
        node = TreeNode(value)
        if self.root is None:
            self.root = node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = node
                    node.parent = current
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    node.parent = current
                    return
                current = current.right

    def search(self, value: T) -> TreeNode[T] | None:
        if self.root is None:
            return None

        current: TreeNode[T] | None = self.root
        while current is not None:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return None

    def remove(self, node: TreeNode[T]) -> None:
        if self.root is None:
            return

        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            elif node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None

            self._nullifyNode(node)
            return

        if node.left is None or node.right is None:
            child: TreeNode[T]
            if node.left is not None:
                child = node.left
            elif node.right is not None:
                child = node.right

            if node.parent is None:
                self.root = child
            elif node.parent.left == node:
                node.parent.left = child
            else:
                node.parent.right = child
            child.parent = node.parent
            self._nullifyNode(node)
            return

        successor: TreeNode[T] = node.right
        while successor.left is not None:
            successor = successor.left
        self.remove(successor)

        if node.parent is None:
            self.root = successor
        elif node.parent.left == node:
            node.parent.left = successor
        else:
            node.parent.right = successor
        successor.parent = node.parent

        successor.left = node.left
        node.left.parent = successor

        successor.right = node.right
        if node.right is not None:
            node.right.parent = successor

        self._nullifyNode(node)

    def _nullifyNode(self, node: TreeNode[T]) -> None:
        node.left = None
        node.right = None
        node.parent = None
