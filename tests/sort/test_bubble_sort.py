from sort.bubble_sort import bubble_sort


def test_bubble_sort() -> None:
    arr = [30, 20, 40, 35, 5, 10, 45, 50, 25, 15]
    bubble_sort(arr)
    assert arr == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
