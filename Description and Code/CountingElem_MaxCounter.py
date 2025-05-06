def solution(N, A):
    counters = [0] * N
    max_val = 0
    last_update = 0

    for operation in A:
        if 1 <= operation <= N:  # increase(X) operation
            index = operation - 1
            # Ensure that the counter is at least as large as last_update before incrementing
            if counters[index] < last_update:
                counters[index] = last_update
            counters[index] += 1
            max_val = max(max_val, counters[index])
        elif operation == N + 1:  # max counter operation
            last_update = max_val

    # After processing all operations, we need to apply any pending max counter updates
    for i in range(N):
        if counters[i] < last_update:
            counters[i] = last_update

    return counters
