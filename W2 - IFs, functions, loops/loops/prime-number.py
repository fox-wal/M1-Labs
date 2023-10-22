prime_numbers = [2]

limit = int(input("I will tell you the prime numbers up to... "))

if limit < 2:
    print("No prime numbers.")
else:
    print(2)

is_prime = True

for current_number in range(3, limit + 1):
    is_prime = True
    for p in prime_numbers:
        # Check if this number is a multiple of a prime number.
        if (current_number % p) == 0:
            is_prime = False
            break
    if not is_prime:
        continue
    prime_numbers.append(current_number)
    print(current_number)