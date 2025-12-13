import sys
import re

input = sys.stdin.readline


def sort_with_two_pointer(a: list[int], b: list[int]) -> list[int]:
    arr: list[int] = []

    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr.append(a[i])
            i += 1
        else:
            arr.append(b[j])
            j += 1

    if i < len(a):
        arr = arr + a[i:]

    if j < len(b):
        arr = arr + b[j:]

    return arr


if __name__ == "__main__":
    n, m = map(int, input().split(" "))

    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))

    sorted_arr = sort_with_two_pointer(a, b)

    formatted_arr = re.sub(r"[\[\],]", "", str(sorted_arr))

    print(formatted_arr)
