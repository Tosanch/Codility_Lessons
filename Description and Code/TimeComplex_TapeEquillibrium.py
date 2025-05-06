def solution(A):
    total = sum(A)
    min_diff = float('inf')
    left_sum = 0

    for P in range(1, len(A)):
        left_sum += A[P - 1]
        right_sum = total - left_sum
        diff = abs(left_sum - right_sum)
        min_diff = min(min_diff, diff)

    return min_diff