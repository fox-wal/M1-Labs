def calculate_lcm(a: int = 1, b: int = 1):
    lcm = 0

    for i in range(1, a + 1):
        lcm = a * i
        if (b % lcm) == 0:
            break

    print("Lowest Common Multiple:", lcm)

def find_primes(limit: int = 0):
    prime_numbers = [2]

    if limit < 2:
        print("No prime numbers.")
        return
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

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
calculate_lcm(a, b)

limit = int(input("I will tell you the prime numbers up to... "))
find_primes(limit)