from sort.insertion_sort import insertion_sort


def test_insertion_sort() -> None:
    arr = [5, 2, 1, 3, 6, 4]
    insertion_sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6]
