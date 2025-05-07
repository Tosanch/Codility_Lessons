import math


def solution(N):
    min_perimeter = float('inf')  # Start with a very large number

    # Loop through all divisors from 1 to sqrt(N)
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:  # If i is a divisor of N
            A = i
            B = N // i
            # Calculate the perimeter for this pair (A, B)
            perimeter = 2 * (A + B)
            # Update the minimum perimeter
            min_perimeter = min(min_perimeter, perimeter)

    return min_perimeter
