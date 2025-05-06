def solution(A, K):
    # Handle edge cases
    if not A or K == 0:
        return A

    N = len(A)
    K = K % N  # Normalize K if it's larger than the array size

    return A[-K:] + A[:-K]
