def combination(n: int, m: int, sequence: list[int] | None = None) -> list[list[int]]:
    if sequence is None:
        sequence = list(range(1, n + 1))

    if m == 0:
        return [[]]

    result: list[list[int]] = []
    for i in range(n):
        v = sequence[i]
        omit_v = sequence[i + 1 :]

        sub_sequence = combination(len(omit_v), m - 1, omit_v)

        for ss in sub_sequence:
            result.append([v] + ss)

    return result


if __name__ == "__main__":
    n, m = map(int, input().split(" "))

    result = combination(n, m)

    [print(" ".join(map(str, r))) for r in result]
