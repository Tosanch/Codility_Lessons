def solution(A):
    # Sort the array first
    A.sort()

    # Iterate through the sorted array and check for triangular triplets
    for i in range(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1  # Found a triangular triplet

    return 0  # No triangular triplet found
