def jump(numbers: list[int]) -> int:
    sum: int = 0
    distance: int | None = None

    for number in numbers:
        if sum + number <= 100:
            sum += number
        else:
            if abs(100 - sum) >= abs(100 - (sum + number)):
                distance = sum + number
            else:
                distance = sum
            break

    if distance is None:
        distance = sum

    return distance


if __name__ == "__main__":
    numbers: list[int] = []
    for _ in range(10):
        number = int(input())
        numbers.append(number)

    distance = jump(numbers)
    print(distance)
