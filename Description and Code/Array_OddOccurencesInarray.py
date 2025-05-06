def solution(A):
    unpaired = 0
    for number in A:
        unpaired ^= number
    return unpaired
