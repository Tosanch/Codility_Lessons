def solution(A):
    N = len(A)
    seen = set()

    for number in A:
        if number < 1 or number > N:
            return 0
        if number in seen:
            return 0
        seen.add(number)

    return 1