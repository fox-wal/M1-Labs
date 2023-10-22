def binary(n: int) -> list[str]:
    if n < 0:
        raise ValueError("Error: input was negative.")
    
    binary_digits = []

    while n > 0:
        binary_digits.append(str(n % 2))
        n = n // 2
    
    return binary_digits

try:
    binary_digits = binary(int(input("Enter number: ")))
except ValueError as e:
    output = e
else:
    output = ""
    for digit in binary_digits:
        output = digit + output
finally:
    print(output)