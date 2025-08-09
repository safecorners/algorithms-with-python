def compute(
    t: int,
    n: int,
    a: list[int],
    m: int,
    b: list[int],
) -> int:
    a = [0] + a
    b = [0] + b

    prefix = {
        "a": [0] * len(a),
        "b": [0] * len(b),
    }

    for i in range(1, len(a)):
        prefix["a"][i] = a[i] + prefix["a"][i - 1]

    for i in range(1, len(b)):
        prefix["b"][i] = b[i] + prefix["b"][i - 1]

    set_a: dict[int, int] = {}
    set_b: dict[int, int] = {}

    # o(n^2)

    for k in range(1, len(a) - 1):
        for i in range(k, len(a)):
            v = prefix["a"][i] - prefix["a"][i - k]
            if v in set_a:
                set_a[v] += 1
            else:
                set_a[v] = 1

    v = prefix["a"][len(a) - 1]
    if v in set_a:
        set_a[v] += 1
    else:
        set_a[v] = 1

    # o(m^2)
    for k in range(1, len(b) - 1):
        for i in range(k, len(b)):
            v = prefix["b"][i] - prefix["b"][i - k]
            if v in set_b:
                set_b[v] += 1
            else:
                set_b[v] = 1

    v = prefix["b"][len(b) - 1]
    if v in set_b:
        set_b[v] += 1
    else:
        set_b[v] = 1

    count = 0

    for v in set_a:
        if t - v in set_b:
            count += set_a[v] * set_b[t - v]

    return count


if __name__ == "__main__":
    t = int(input())
    n = int(input())
    a = list(map(int, input().split(" ")))
    m = int(input())
    b = list(map(int, input().split(" ")))

    count = compute(t, n, a, m, b)

    print(count)
