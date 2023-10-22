def binary(n: int) -> list[str]:
    if n < 0:
        print("Error: input was negative.")
        return []
    
    binary_digits = []

    while n > 0:
        binary_digits.append(str(n % 2))
        n = n // 2
    
    return binary_digits

binary_digits = binary(int(input("Enter number: ")))

output = ""
for digit in binary_digits:
    output = digit + output

print(output)