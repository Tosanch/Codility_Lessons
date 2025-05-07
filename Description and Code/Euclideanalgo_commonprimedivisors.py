import math


# Function to get the prime divisors of a number
def get_prime_divisors(num):
    divisors = set()

    # Check for divisibility by 2
    while num % 2 == 0:
        divisors.add(2)
        num //= 2

    # Check for divisibility by odd numbers from 3 to sqrt(num)
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            divisors.add(i)
            num //= i

    # If num is still greater than 2, it's prime
    if num > 2:
        divisors.add(num)

    return divisors


# Main solution function
def solution(A, B):
    count = 0

    # Iterate through each pair (A[i], B[i]) and compare their prime divisors
    for i in range(len(A)):
        prime_divisors_A = get_prime_divisors(A[i])
        prime_divisors_B = get_prime_divisors(B[i])

        # Compare the prime divisors sets
        if prime_divisors_A == prime_divisors_B:
            count += 1

    return count
