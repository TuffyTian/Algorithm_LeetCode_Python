def reverse(x: int) -> int:
    min_number = -2**31
    max_number = 2**31 - 1
    if x < min_number or x > max_number:
        return 0

    is_nagative = False
    if x < 0:
        is_nagative = True
        x = x * (-1)

    result = x % 10
    remainder = int(x / 10)
    while remainder != 0:
        result = result * 10 + remainder % 10
        remainder = int(remainder / 10)

    if is_nagative:
        result = result * (-1)
    return result


if __name__ == "__main__":
    print(reverse(123))