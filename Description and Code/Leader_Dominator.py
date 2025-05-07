def solution(A):
    size = 0
    candidate = None

    # Phase 1: Find candidate
    for value in A:
        if size == 0:
            candidate = value
            size = 1
        else:
            size += 1 if value == candidate else -1

    # Phase 2: Confirm candidate is dominator
    if candidate is None:
        return -1

    count = A.count(candidate)
    if count > len(A) // 2:
        # Return any index of the dominator
        for index, value in enumerate(A):
            if value == candidate:
                return index
    return -1
