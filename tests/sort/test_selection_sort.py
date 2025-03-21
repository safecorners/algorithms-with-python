from sort.selection_sort import selection_sort


def test_selection_sort() -> None:
    arr = [30, 20, 40, 35, 5, 10, 45, 50, 25, 15]
    selection_sort(arr)
    assert arr == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
