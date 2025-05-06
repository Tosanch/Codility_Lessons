def solution(X, A):
    positions = set()
    for time, pos in enumerate(A):
        if pos <= X:
            positions.add(pos)
            if len(positions) == X:
                return time
    return -1
