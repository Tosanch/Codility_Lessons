def solution(A):
    min_avg = float('inf')
    min_index = 0
    N = len(A)

    for i in range(N - 1):
        # Check 2-element slice
        avg2 = (A[i] + A[i + 1]) / 2
        if avg2 < min_avg:
            min_avg = avg2
            min_index = i

        # Check 3-element slice
        if i < N - 2:
            avg3 = (A[i] + A[i + 1] + A[i + 2]) / 3
            if avg3 < min_avg:
                min_avg = avg3
                min_index = i

    return min_index
