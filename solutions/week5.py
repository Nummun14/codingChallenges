import math


def reversed_factorial(factorial):
    num = 1
    while math.factorial(num) < factorial:
        num += 1

    if math.factorial(num) == factorial:
        return num
    return -1


def most_efficient_reversed_factorial(factorial):
    num = 1
    while factorial % num == 0:
        factorial //= num
        num += 1

    return num - 1 if factorial == 1 else -1


reversed_factorial(120)
# יחזיר 5
reversed_factorial(24)
# יחזיר 4
reversed_factorial(150)
# יחזיר -1
reversed_factorial(1)
# יחזיר 1
