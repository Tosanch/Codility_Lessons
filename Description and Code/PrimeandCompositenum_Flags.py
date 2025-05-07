def solution(A):
    N = len(A)

    # Step 1: Identify peaks
    peaks = []
    for i in range(1, N - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peaks.append(i)

    # Number of peaks found
    P = len(peaks)

    if P == 0:
        return 0  # No peaks, so no flags can be placed

    # Step 2: Binary search on the number of flags (K)
    def can_place_flags(K):
        # Try to place K flags with at least K distance between them
        flags_placed = 1  # Place the first flag on the first peak
        last_position = peaks[0]

        for i in range(1, P):
            if peaks[i] - last_position >= K:
                flags_placed += 1
                last_position = peaks[i]
            if flags_placed == K:
                return True
        return False

    # Binary search to find the maximum number of flags
    left, right = 1, P
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_place_flags(mid):
            result = mid  # It's possible to place 'mid' flags, try for more
            left = mid + 1
        else:
            right = mid - 1

    return result
