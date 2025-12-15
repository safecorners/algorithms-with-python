def permutation(n: int, r: int, sequence: list[int]) -> list[list[int]]:
    if r == 0:
        return [[]]
    permutations: list[list[int]] = []
    for i in range(n):
        sub_permutations = permutation(n - 1, r - 1, sequence[:i] + sequence[i + 1 :])

        for sp in sub_permutations:
            permutations.append([sequence[i]] + sp)
    return permutations


if __name__ == "__main__":
    permutations = permutation(9, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    sample_space = set([tuple(p) for p in permutations])

    n = int(input())

    for _ in range(n):
        q, s, b = map(int, input().split(" "))
        t = tuple([int(digit) for digit in str(q)])

        a1, a2, a3 = t
        if s == 3:
            sample_space = sample_space & set([(a1, a2, a3)])

        if s == 2 and b == 0:
            possible_number = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set([a1, a2, a3]))
            possible_sequence = set(
                [(a1, a2, p) for p in possible_number]
                + [(a1, p, a3) for p in possible_number]
                + [(p, a2, a3) for p in possible_number]
            )
            sample_space = sample_space & possible_sequence

        if s == 1 and b == 2:
            possible_sequence = set(
                [
                    (a1, a3, a2),
                    (a3, a2, a1),
                    (a2, a1, a3),
                ]
            )
            sample_space = sample_space & possible_sequence

        if s == 1 and b == 1:
            possible_number = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set([a1, a2, a3]))
            possible_sequence = set(
                [(a1, p, a2) for p in possible_number]
                + [(a1, a3, p) for p in possible_number]
                + [(p, a2, a1) for p in possible_number]
                + [(a3, a2, p) for p in possible_number]
                + [(a2, p, a3) for p in possible_number]
                + [(p, a1, a3) for p in possible_number]
            )
            sample_space = sample_space & possible_sequence

        if s == 1 and b == 0:
            possible_number = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set([a1, a2, a3]))
            possible_permutations = permutation(6, 2, possible_number)
            possible_sequence = set(
                [(a1, p1, p2) for (p1, p2) in possible_permutations]
                + [(p1, a2, p2) for (p1, p2) in possible_permutations]
                + [(p1, p2, a3) for (p1, p2) in possible_permutations]
            )
            sample_space = sample_space & possible_sequence

        if s == 0 and b == 3:
            possible_sequence = set(
                [
                    (a3, a1, a2),
                    (a2, a3, a1),
                ]
            )
            sample_space = sample_space & possible_sequence
        if s == 0 and b == 2:
            possible_number = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set([a1, a2, a3]))
            possible_sequence = set(
                [(p1, a3, a2) for p1 in possible_number]
                + [(a2, a3, p1) for p1 in possible_number]
                + [(a3, p1, a2) for p1 in possible_number]
                + [(a3, a1, p1) for p1 in possible_number]
                + [(p1, a3, a1) for p1 in possible_number]
                + [(a3, p1, a1) for p1 in possible_number]
                + [(p1, a1, a2) for p1 in possible_number]
                + [(a2, a1, p1) for p1 in possible_number]
                + [(a2, p1, a1) for p1 in possible_number]
            )
            sample_space = sample_space & possible_sequence

        if s == 0 and b == 1:
            possible_number = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set([a1, a2, a3]))
            possible_permutations = permutation(6, 2, possible_number)
            possible_sequence = set(
                [(p1, p2, a1) for (p1, p2) in possible_permutations]
                + [(p1, a1, p2) for (p1, p2) in possible_permutations]
                + [(a2, p1, p2) for (p1, p2) in possible_permutations]
                + [(p1, p2, a2) for (p1, p2) in possible_permutations]
                + [(a3, p1, p2) for (p1, p2) in possible_permutations]
                + [(p1, a3, p2) for (p1, p2) in possible_permutations]
            )
            sample_space = sample_space & possible_sequence

        if s == 0 and b == 0:
            possible_number = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set([a1, a2, a3]))
            possible_permutations = permutation(6, 3, possible_number)
            possible_sequence = set(
                [(p1, p2, p3) for p1, p2, p3 in possible_permutations]
            )
            sample_space = sample_space & possible_sequence

    print(len(sample_space))
