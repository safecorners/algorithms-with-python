def distribute(candy: int) -> int:
    outcomes = 0
    for a in range(0, candy + 1):
        for b in range(0, candy + 1):
            for c in range(0, candy + 1):
                if (
                    (a + b + c == candy)
                    and (a >= b + 2)
                    and (c % 2 == 0)
                    and a > 0
                    and b > 0
                    and c > 0
                ):
                    outcomes = outcomes + 1

    return outcomes


if __name__ == "__main__":
    candy = int(input())

    outcomes = distribute(candy)

    print(outcomes)
