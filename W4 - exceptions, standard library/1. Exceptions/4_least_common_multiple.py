def calculate_lcm(a: int, b: int):
    if (a < 0) or (b < 0):
        raise ValueError("a and b must both be positive")

    lcm = 0

    for i in range(1, a + 1):
        lcm = a * i
        if (b % lcm) == 0:
            break

    return lcm

try:
    print("Lowest Common Multiple:", calculate_lcm(6, 0))
except ValueError as e:
    print(e)