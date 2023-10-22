a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

factors_of_a = []

for i in range(2, a):
    if (a % i) == 0:
        factors_of_a.append(i)

hcf = 1
for f in factors_of_a:
    if (a % f) == 0:
        hcf = f

lcm = a / hcf * b

print("Lowest Common Multiple:", int(lcm))