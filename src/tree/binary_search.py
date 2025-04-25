def binary_search(arr: list[int], low: int, high: int, target: int) -> int | None:
    if low > high:
        return None

    mid = (low + high) // 2
    if arr[mid] == target:
        return arr[mid]

    if arr[mid] > target:
        return binary_search(arr, 0, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)
