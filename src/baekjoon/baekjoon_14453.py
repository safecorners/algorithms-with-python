def maximize_winning(n: int, gestures: list[str]) -> int:
    gestures = [""] + gestures + [""]

    prefix: dict[str, list[int]] = {
        "P": [0] * len(gestures),
        "H": [0] * len(gestures),
        "S": [0] * len(gestures),
    }

    suffix: dict[str, list[int]] = {
        "P": [0] * len(gestures),
        "H": [0] * len(gestures),
        "S": [0] * len(gestures),
    }

    for i in range(1, len(gestures)):
        prefix["P"][i] = prefix["P"][i - 1] + (1 if gestures[i] == "P" else 0)
        prefix["H"][i] = prefix["H"][i - 1] + (1 if gestures[i] == "H" else 0)
        prefix["S"][i] = prefix["S"][i - 1] + (1 if gestures[i] == "S" else 0)

    for i in range(len(gestures) - 2, 0, -1):
        suffix["P"][i] = suffix["P"][i + 1] + (1 if gestures[i] == "P" else 0)
        suffix["H"][i] = suffix["H"][i + 1] + (1 if gestures[i] == "H" else 0)
        suffix["S"][i] = suffix["S"][i + 1] + (1 if gestures[i] == "S" else 0)

    wins = [0] * len(gestures)

    for i in range(1, len(gestures) - 1):
        prefix_max = max(
            prefix["P"][i],
            prefix["H"][i],
            prefix["S"][i],
        )

        suffix_max = max(
            suffix["P"][i + 1],
            suffix["H"][i + 1],
            suffix["S"][i + 1],
        )

        wins[i] = prefix_max + suffix_max

    return max(wins)


if __name__ == "__main__":
    n = int(input())

    seq = [input() for _ in range(n)]

    result = maximize_winning(n, seq)
    print(result)
