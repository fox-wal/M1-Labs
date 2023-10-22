#
# Task 3: Division using subtraction
#

p = int(input("Enter a number: "))
q = int(input("Enter a number: "))

remainder = p
quotient = 0

while (remainder - q) >= 0:
    remainder -= q
    quotient += 1

print(p, "/", q, "=", quotient, "remainder", remainder)