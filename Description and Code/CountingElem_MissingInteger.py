def solution(A):
    N = len(A)

    # Step 1: Ignore numbers outside the range [1, N]
    for i in range(N):
        if A[i] <= 0 or A[i] > N:
            A[i] = N + 1  # Replace invalid numbers with a number larger than N

    # Step 2: Use the array itself for marking presence
    for i in range(N):
        val = abs(A[i])  # We work with absolute value to handle marking
        if 1 <= val <= N:
            # Mark the index val - 1 as negative to indicate that val is present
            if A[val - 1] > 0:
                A[val - 1] = -A[val - 1]

    # Step 3: Find the first index with a positive value, which means the corresponding number is missing
    for i in range(N):
        if A[i] > 0:
            return i + 1  # The missing number is i + 1

    # Step 4: If all numbers 1 to N are present, the missing number is N + 1
    return N + 1
