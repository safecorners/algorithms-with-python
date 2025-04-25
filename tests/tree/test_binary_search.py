from tree.binary_search import binary_search
from tree.iterative_binary_search import iterative_binary_search


def test_binary_search() -> None:
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 0, len(arr) - 1, 3) == 3
    assert binary_search(arr, 0, len(arr) - 1, -1) is None
    assert binary_search(arr, 0, len(arr) - 1, 1) == 1
    assert binary_search(arr, 0, len(arr) - 1, 5) == 5


def test_binary_search_not_found() -> None:
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 0, len(arr) - 1, 6) is None


def test_supports_comparion() -> None:
    arr = ["a", "b", "c", "d", "e"]
    assert iterative_binary_search(arr, "c") == "c"


def test_iterative_binary_search() -> None:
    arr = [1, 2, 3, 4, 5]
    assert iterative_binary_search(arr, 3) == 3
    assert iterative_binary_search(arr, -1) is None
    assert iterative_binary_search(arr, 1) == 1
    assert iterative_binary_search(arr, 5) == 5
