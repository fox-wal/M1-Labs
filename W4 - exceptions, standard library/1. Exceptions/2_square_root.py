from math import sqrt

def calc_sqrt(k: int):
    '''
    Calculates the square root of the given number.

    Args:
        k: The number whose square root will be calculated.
    
    Returns:
        The square root of `k`.

    Exceptions:
        ValueError: if `k` is negative.
    '''
    if k < 0:
        raise ValueError("Cannot square root a negative number.")
    
    return sqrt(k)

print("Calculate Square Root")
try:
    square_number = float(input("Enter number: "))
    result = calc_sqrt(square_number)
except ValueError as e:
    print(e)
else:
    print("Square root:", result)
finally:
    print("End of program.")