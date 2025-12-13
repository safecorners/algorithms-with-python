from typing import Generator


def infinite() -> Generator[int, None, None]:
    number = 1
    while True:
        yield number
        number += 1


def compute(n: int) -> int:
    numbers: dict[int, bool] = {}
    count = 0

    for number in infinite():
        is_repeated = False
        string = str(number)
        length = len(string)

        for i in range(length):
            for j in range(i + 1, length + 1):
                substring = string[i:j]
                if substring in string:
                    is_repeated = True

        if is_repeated is False:
            count += 1

        if count == n:
            return number

    return number


if __name__ == "main":
    while True:
        number = int(input())

        if number == 0:
            exit()

        compute(number)
