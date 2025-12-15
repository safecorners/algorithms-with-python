from baekjoon.baekjoon_2503 import permutation


def test_split_into_tuple() -> None:
    q = 429
    w = tuple([int(digit) for digit in str(q)])
    assert w == (4, 2, 9)


def test_permutation() -> None:
    ss = set(
        [tuple(sample) for sample in permutation(9, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])]
    )

    print(ss)


def test_list() -> None:
    a1, a2, a3 = 1, 2, 3
    possible_number = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set([a1, a2, a3]))
    s = set(
        [(a1, a2, p) for p in possible_number]
        + [(a1, p, a3) for p in possible_number]
        + [(p, a2, a3) for p in possible_number]
    )
    print("")
    print(sorted(list(s)))
