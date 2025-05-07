def solution(A):
    N = len(A)

    # Step 1: Create frequency array
    max_value = 2 * N  # the maximum value in A can be up to 2*N
    freq = [0] * (max_value + 1)  # Frequency array

    # Fill the frequency array
    for number in A:
        freq[number] += 1

    # Step 2: Calculate non-divisors for each element in A
    result = []

    for num in A:
        non_divisors = N  # start with all elements
        # Subtract the number of divisors of num
        for i in range(1, int(num ** 0.5) + 1):  # divisors up to sqrt(num)
            if num % i == 0:  # i is a divisor
                # Check if i is in the array
                non_divisors -= freq[i]
                # Also check for the paired divisor num // i
                if i != num // i:
                    non_divisors -= freq[num // i]

        result.append(non_divisors)

    return result
