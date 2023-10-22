#
# Task 3: Exponent using multiplication
#

number = int(input("Enter a number: "))
exponent = int(input("Enter an exponent: "))

result = 1
for i in range(exponent):
    result *= number

print(number, "^", exponent, "=", result)