from typing import Generator

count = 0


def takhee() -> Generator[int, None, None]:
    num = 0
    while True:
        num += 2
        yield num


def distribute(candy: int) -> None:
    for a in takhee():
        for b in range(1, candy - a + 1):
            for c in range(b + 2, candy - b + 2):
                if a + b + c == candy:
                    global count
                    count += 1

        if a > candy:
            break


if __name__ == "__main__":
    candy = int(input())

    distribute(candy)

    print(count)
