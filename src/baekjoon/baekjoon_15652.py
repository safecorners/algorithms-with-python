def non_dec_seq(
    n: int,
    m: int,
    seq: list[int] | None = None,
) -> list[list[int]]:
    if seq is None:
        seq = list(range(1, n + 1))

    if m == 0:
        return [[]]

    result: list[list[int]] = []
    for i in range(n):
        v = seq[i]

        sub_seq = non_dec_seq(n - i, m - 1, seq[i:])

        result = result + [[v] + ss for ss in sub_seq]

    return result


if __name__ == "__main__":
    n, m = map(int, input().split(" "))

    result = non_dec_seq(n, m)

    [print(" ".join(map(str, r))) for r in result]
