import math

def solution(N):
    count = 0
    # Loop through all numbers from 1 to sqrt(N)
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:  # If i is a divisor of N
            count += 1  # Count i as a divisor
            if i != N // i:  # Avoid counting the square root twice
                count += 1  # Count N // i as a divisor
    return count
