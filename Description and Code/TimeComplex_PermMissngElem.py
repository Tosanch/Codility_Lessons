def solution(A):
    N = len(A)
    expected_sum = (N + 1) * (N + 2) // 2
    actual_sum = sum(A)
    return expected_sum - actual_sum