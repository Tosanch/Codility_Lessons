def solution(S, P, Q):
    N = len(S)
    M = len(P)

    # Prefix sums for A, C, G
    prefix_A = [0] * (N + 1)
    prefix_C = [0] * (N + 1)
    prefix_G = [0] * (N + 1)

    for i in range(N):
        prefix_A[i + 1] = prefix_A[i] + (1 if S[i] == 'A' else 0)
        prefix_C[i + 1] = prefix_C[i] + (1 if S[i] == 'C' else 0)
        prefix_G[i + 1] = prefix_G[i] + (1 if S[i] == 'G' else 0)

    result = []
    for i in range(M):
        start = P[i]
        end = Q[i] + 1  # for inclusive range

        if prefix_A[end] - prefix_A[start] > 0:
            result.append(1)
        elif prefix_C[end] - prefix_C[start] > 0:
            result.append(2)
        elif prefix_G[end] - prefix_G[start] > 0:
            result.append(3)
        else:
            result.append(4)

    return result
