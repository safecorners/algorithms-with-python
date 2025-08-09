def sum(items: list[int]) -> int:
    total = 0
    for item in items:
        total += item
    return total


def pick(n: int, m: int, dwarfs: list[int]) -> list[list[int]]:
    if m == 0:
        return [[]]

    result: list[list[int]] = []

    for i in range(n):
        v = dwarfs[i]
        omit_v = dwarfs[i + 1 :]

        sub_sequence = pick(len(omit_v), m - 1, omit_v)

        for ss in sub_sequence:
            sequence = [v] + ss
            if sum(sequence) <= 100:
                result.append(sequence)

    return result


if __name__ == "__main__":
    dwarfs: list[int] = []
    for _ in range(9):
        dwarfs.append(int(input()))

    dwarfs.sort()

    results = pick(9, 7, dwarfs)
    filtered = [result for result in results if sum(result) == 100]

    for item in filtered[0]:
        print(item)
