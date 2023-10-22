a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

lcm = 0

for i in range(1, a + 1):
    lcm = a * i
    if (b % lcm) == 0:
        break

print("Lowest Common Multiple:", lcm)