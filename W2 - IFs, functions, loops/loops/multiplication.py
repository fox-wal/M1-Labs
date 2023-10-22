#
# Task 3: Multiplication using addition
#

n = int(input("Enter a number: "))
m = int(input("Enter a number: "))

result = 0
for i in range(n):
    result += m

print(n, "x", m, "=", result)