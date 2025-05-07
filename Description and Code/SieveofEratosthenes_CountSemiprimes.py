def solution(N, P, Q):
    # Step 1: Use Sieve of Eratosthenes to find all primes up to N
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, N + 1) if is_prime[i]]

    # Step 2: Find all semiprimes up to N
    semiprimes = [False] * (N + 1)
    for i in range(len(primes)):
        for j in range(i, len(primes)):  # To include square primes (p * p)
            semiprime = primes[i] * primes[j]
            if semiprime > N:
                break
            semiprimes[semiprime] = True

    # Step 3: Create a prefix sum array for semiprimes
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (1 if semiprimes[i] else 0)

    # Step 4: Answer the queries using the prefix sum array
    result = []
    for i in range(len(P)):
        left = P[i]
        right = Q[i]
        result.append(prefix_sum[right] - prefix_sum[left - 1])

    return result
